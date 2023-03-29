import json
import os
from rest_framework import generics, permissions

from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.base import ContentFile
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.db.models import Q
from mptt.forms import MoveNodeForm, TreeNodeChoiceField

from . import serializers
from .permisisions import IsOwnerOrReadOnly
from .models import Object, Picture, Category, Storage
from .forms import ObjForm, PicForm, FilterForm, ObjUpdateForm
from .filters import ObjFilter



class AccountIndex(LoginRequiredMixin, TemplateView):
    '''Личный кабинет'''
    template_name = 'object/account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count_obj'] = Object.objects.filter(owner=self.request.user).count()
        return context


def index(request):
    '''Главная страница'''
    data = 'Сайт'
    count_obj = Object.objects.filter(owner=request.user.id).count() if request.user else None
    return render(request, 'object/index.html', {
        'data': data,
        'count_obj': count_obj,
        })


class CategoryListView(ListView):
    '''Строит дерево категорий'''
    model = Category
    template_name = 'object/category_list.html'



class CategoryDetailView(LoginRequiredMixin, DetailView):
    '''Выводит вещи из выбранной категории'''
    model = Category
    template_name = "object/category_obj.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj_user = Object.objects.filter(owner=self.request.user)
        cat_children = Category.objects.get(pk=self.kwargs['pk']).get_descendants(include_self=True)
        context['things'] = Object.objects.filter(category__in=cat_children)
        context['photos'] = Picture.objects.filter(obj__owner=self.request.user)
        context['cat_user'] = Category.objects.filter(object__in=obj_user).distinct().get_ancestors(include_self=True)
        return context


# class ObjUpdateView(LoginRequiredMixin, UpdateView):
#     '''Редактирование вещи'''
#     model = Object
#     template_name = 'object/obj_edit.html'
#     fields = ['name', 'description', 'category', 'storage']
#     success_url = reverse_lazy('home')

@login_required
def obj_update(request, pk):
    '''Редактирование вещи'''
    context ={}
    if request.method == 'GET':
        obj = Object.objects.get(id=pk)
        pic = Picture.objects.filter(obj=obj)

        date = {
            'name': obj.name,
            'description': obj.description,
            'category': obj.category,
            'storage': obj.storage,
        }
        form = ObjUpdateForm(date)
        context["photos"] = pic

    elif request.method == 'POST':
        form = ObjUpdateForm(request.POST, request.FILES)
        print('post', form.is_valid())
        print(request.POST)
        if form.is_valid():
            print('valid')
            obj = Object.objects.filter(id=pk).update(
            name = form.cleaned_data['name'],
            description = form.cleaned_data['description'],
            category = form.cleaned_data['category'],
            storage = form.cleaned_data['storage'],
            )
            print('request.FILES', request.FILES)
            if request.FILES:
                for file in request.FILES.getlist('photos'):
                    data = file.read()
                    photo = Picture(obj=Object.objects.get(id=pk))
                    photo.image.save(file.name, ContentFile(data))
                    photo.save()
        return redirect('obj_detail', pk=pk)

    context["form"] = form
    # return render(request, "object/page8.html", context)
    return render(request, "object/obj_edit.html", context)


@login_required
def obj_add(request):
    '''Добавить вещь'''
    if request.method == 'GET':
        form = ObjForm()
    elif request.method == 'POST':
        form = ObjForm(request.POST, request.FILES)
        print(request.POST)
        print(request.FILES)
        if form.is_valid():
            print('Form true')
            obj = Object.objects.create(
                owner=request.user,
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                category=form.cleaned_data['category'],
                storage=form.cleaned_data['storage'],
                )
            for f in request.FILES.getlist('photos'):
                data = f.read()
                photo = Picture(obj=obj)
                photo.image.save(f.name, ContentFile(data))
                photo.save()
            return redirect('obj_detail', pk=obj.pk)
        else:
            print('Form false')
            form = ObjForm()
    return render(request, 'object/obj_add.html', {'form': form})

@login_required
def obj_detail(request, pk):
    '''Посмотреть вещь'''
    obj = get_object_or_404(Object, pk=pk)
    photos = Picture.objects.filter(obj=pk)
    obj_path = Category.objects.filter(object=obj).get_ancestors(include_self=True)
    return render(request, 'object/obj_detail.html', {
    # return render(request, 'object/page6.html', {
        'obj': obj, 
        'photos': photos,
        'obj_path': obj_path,
        })

@login_required
def pic_del(request, pk):
    '''Удалить фото'''
    pic = Picture.objects.get(id=pk)
    pk = pic.obj.id
    pic.delete()
    return redirect('obj_detail', pk=pk)


class ObjDeleteView(LoginRequiredMixin, DeleteView):
    '''Удалить вещь'''
    model = Object
    template_name = 'object/obj_delete.html'
    success_url = reverse_lazy('obj_list')


class ObjListView(LoginRequiredMixin, ListView):
    '''Список вещей пользователя'''
    model = Object
    template_name = 'object/obj_list.html'
    # template_name = 'object/page4.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ObjFilter(self.request.GET, queryset=Object.objects.filter(owner=self.request.user))
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        obj_user = Object.objects.filter(owner=self.request.user)
        context = super().get_context_data(**kwargs)
        context['filter'] = FilterForm(self.request.GET, obj_user=obj_user)
        context['photos'] = Picture.objects.filter(obj__in=obj_user)
        context['cat_user'] = Category.objects.filter(object__in=obj_user).distinct().get_ancestors(include_self=True)
        return context


@login_required
def add_pic(request, pk):
    '''Кнопка добавления картинки'''
    if request.method == 'POST':
        form = PicForm(request.POST, request.FILES)
        if form.is_valid():
            for f in request.FILES.getlist('photos'):
                data = f.read()
                photo = Picture(obj=Object.objects.get(id=pk))
                photo.image.save(f.name, ContentFile(data))
                photo.save()
            return redirect('obj_detail', pk=pk)
    else:
        form = PicForm()
    return redirect('obj_detail', pk=pk)


class SearchObject(LoginRequiredMixin, ListView):
    '''Страница поиска'''
    model = Object
    template_name = 'object/search.html'

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('q')
        context = super().get_context_data(**kwargs)
        context['search_result'] = Object.objects.filter(name__icontains=query)
        # context['pic'] = Picture.objects.filter(obj=pk)

        return context


class ObjPublic(DetailView):
    '''Подробное описание вещи для всех пользователей'''
    model = Object
    template_name = 'object/obj_public.html'
    
    def get_context_data(self, **kwargs):
        pk=self.kwargs['pk']
        obj = Object.objects.get(pk=pk)
        photos = Picture.objects.filter(obj=obj)
        context = super().get_context_data(**kwargs)
        context['obj'] = obj
        context['list_photos_count'] = [i for i in range(1, photos.count() + 1)]
        context['photos'] = photos
        
        return context


class StorageList(LoginRequiredMixin, ListView):
    '''Список мест хранения'''
    model = Storage
    template_name = 'object/storage_list.html'
    context_object_name = 'storage_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['storage_list'] = Storage.objects.filter(user = self.request.user)
        return context


class StorageDetail(LoginRequiredMixin, DetailView):
    '''Список вещей в выбраном месте хранения'''
    model = Storage
    template_name = 'object/storage_detail.html'

    def get_context_data(self, **kwargs):
        pk=self.kwargs['pk']
        storage = Storage.objects.get(pk=pk)
        obj = Object.objects.filter(storage=storage)
        context = super().get_context_data(**kwargs)
        context['obj'] = obj
        context['storage'] = storage
        context['photos'] = Picture.objects.filter(obj__in=obj)
        return context


class StorageDelete(LoginRequiredMixin, DeleteView):
    '''Удалить место хранения'''
    model = Storage
    template_name = 'object/storage_delete.html'
    success_url = reverse_lazy('storage_list')


class StorageUpdate(LoginRequiredMixin, UpdateView):
    '''Редактировать место хранения'''
    model = Storage
    template_name = 'object/storage_edit.html'
    fields = ['name']
    success_url = reverse_lazy('storage_list')


class StorageCreate(LoginRequiredMixin, CreateView):
    '''Добавление места хранения'''
    model = Storage
    template_name = 'object/storage_create.html'
    fields = ['name']
    success_url = reverse_lazy('obl_list')

    def form_valid(self, form):
        print(self)
        storage = form.save(commit=False)
        storage.user = self.request.user
        return super().form_valid(form)


'''Дальше идёт код для загрузки БД. После заливки удалить'''

def set_parent(request):   # заполняем parent
    categoties = Category.objects.all()
    for cat in categoties:
        try:
            id_parent = Category.objects.get(id_old=cat.id_parent_old)
            cat.parent = id_parent
            cat.save()
            print(cat.id, cat.name, cat.id_old, cat.id_parent_old, )
        except:
            print('Нет объекта с id_old', cat.id_parent_old, (cat.name))
    data = Category.objects.all()
    return render(request, "object/index.html", {'data': data})


def load_cat(request):   # выгружаем из json файла и записываем в базу
    print(os.getcwd ())
    loads = ''
    with open('./category-lv-new.json', 'r', encoding='utf-8') as f:
        loads = f.read()
    cat_dict = json.loads(loads)   # получаем словарь {id_old: [<название категории>, id_parent_old]}

    for cat in cat_dict:
        print(cat, '/', cat_dict[cat][0], '/', cat_dict[cat][1])
        Category.objects.create(
            name=cat_dict[cat][0], 
            id_old=cat, 
            id_parent_old=cat_dict[cat][1]
            )
        

    data = Category.objects.all()

    return render(request, "object/index.html", {'data': data})
    

'''Конец блока для загрузки БД'''