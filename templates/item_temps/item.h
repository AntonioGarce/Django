{% include "header.html" %} {% autoescape off %}
{% load custom_filter %}

<div class="body-wrapper">

<div>
<div class="breadcrumb-area">
<div class="container">
<div class="breadcrumb-content">
<ul>
<li><a href="{% url 'index' %}">Главная</a></li>
<li>
<a href="{% url 'products' %}">
Товары
</a>
</li>
<li>
<a class="active">
 {{item.name}}
</a>
</li>
</ul>
</div>
</div>
</div>
<div class="content-wraper pb-60">
<div class="container">
<div class="card mt-3">
<div class="card-body">
<div class="row align-items-center">
<div class="col-md-2">
<div class="d-flex align-items-center justify-content-center">
<img src="{{ item.store.img.url }}" width="80" alt="">
</div>
</div>
<div class="col-md-10">
<h4>

 <img width="13px" src="./item_files/crown.svg" alt="">

<a href="{% url 'store_page' item.store.id %}"><u>{{ item.store }}</u></a>
</h4>
<p>
<span class="">
<span>Продаж: <strong>{{ item.store.sold }}</strong></span>
</span>
<span class="ml-25">
<span>Рейтинг: <strong>{{ item.store.rating }}</strong></span>
</span>
<span class="ml-25">
<span>Депозит:
<strong>{{ item.store.deposit }}</strong>
<i class="fa fa-btc"></i>
</span>
</span>
 <span class="ml-25">
<span>Категория:
<strong>{{ item.store.store_type }}</strong>
<i class="fa fa-btc"></i>
</span>
</span>
</p>
<div class="d-flex">
<div class="d-flex align-items-center justify-content-between">
<div class="" style="font-size:16px">
<a href="{% url 'store_rules' item.store.id %}" class="">Правила магазина</a>
<a href="{% url 'store_page' item.store.id %}" class="ml-25">Отзывы магазина</a>
<strong>
<a style="{% url 'store_work' item.store %}" href="{% url 'store_work' item.store.id %}" class="ml-25">Работа</a>
</strong>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="row single-product-area">
<div class="col-lg-6 col-md-5">
<div class="product-details-view-content sp-affiliate-content pt-45">
<div class="product-info">
<div class="d-flex justify-content-between">
<h1>{{item.name}}</h1>
</div>
<span class="product-details-ref mb-2 d-block">
<a href="">
{{ item.category_name}}
</a>
</span>
<span class="d-block product-details-ref">
<svg width="1em" fill="#a4a4a4" enable-background="new 0 0 395.71 395.71" version="1.1" viewBox="0 0 395.71 395.71" xml:space="preserve" xmlns="http://www.w3.org/2000/svg">
<path d="m197.85 0c-75.718 0-137.32 61.609-137.32 137.33 0 72.887 124.59 243.18 129.9 250.39l4.951 6.738c0.579 0.792 1.501 1.255 2.471 1.255 0.985 0 1.901-0.463 2.486-1.255l4.948-6.738c5.308-7.211 129.9-177.5 129.9-250.39 0-75.72-61.61-137.33-137.33-137.33zm0 88.138c27.13 0 49.191 22.062 49.191 49.191 0 27.115-22.062 49.191-49.191 49.191-27.114 0-49.191-22.076-49.191-49.191 0-27.129 22.076-49.191 49.191-49.191z"></path>
</svg>

 {% for i in cities_ar %}
<span>{{ i }}</span>
 {% endfor %}
</span>
<div class="price-box pt-10">
от
<span style="" class="new-price"><strong>{{ item.min_price }}</strong> ₽</span>
<span class="ml-2">/
{{item.amount}}
</span>
<span class="sub-price">
~{{ item.min_price|divide:kurs }}
<i class="fa fa-btc" aria-hidden="true"></i>
</span>
</div>
<div class="product-desc">
<input type="checkbox" class="read-more-checker" id="read-more-checker">
<div class="limiter">
 {{ item.description }}
<div class="bottom"></div>
</div>
<label for="read-more-checker" class="read-more-button"></label>
</div>
<div class="d-flex ">
<a class="product-action-link mr-3" href="">
<span style="vertical-align: middle;">Написать продавцу</span>
</a>

</div>
</div>
</div>
</div>
<div class="col-lg-4 col-md-5">
<div class="product-details-left">
<div class="product-details-images">
<div class="lg-image pt-md-5 pt-3 pt-md-45">
 {% if item.img %}
<img src="{{ item.img.url }}" alt="Product Image">
 {% endif %}
</div>
</div>
</div>
</div>
<div class="col-lg-2 col-md-2 d-flex justify-content-end">
<div class="pt-45 d-flex flex-column" style="max-width: 120px">
<div class="card">
<div class="card-body text-center">
<h2>
 {{ item.rating }}
</h2>
<p>рейтинг</p>
</div>
</div>
<div class="card mt-2">
<div class="card-body text-center d-flex align-items-center justify-content-center">
<form action="{% url 'item' category BD %}" method="post">
 {% csrf_token %}
<input type="hidden" name="_token" value="BAG4OCmgaACHs5LGldQIypDICiJe5wLzNKJds8i7"> <input type="hidden" name="_method" value="put"> <h2>
<i class="fa fa-heart-o" aria-hidden="true"></i>
</h2>
<input type="submit" name='action' value="Закладки">
</form>
</div>
</div>
</div>
</div>
</div>
<div class="pt-45 pb-15">
<div class="col-12 p-0">
<form action="">
<div class="">
<div class="mb-3">
<select name="city" class="form-control  form-control-sm" id="change_city">
<option value="">Доступные города:</option>
<option value="5920">
 {{item.cities}}

</select>
</div>
<button type="submit" class="button custom-btn__black mb-3 w-100">
Изменить город
</button>
 </div>
</form>
</div>
<div class="col-12 p-0">
<div class="table-content table-responsive custom-scrollbar" style="max-height: 425px;">
<table class="table">
<thead>
<tr>
<th scope="col">Локация</th>
<th scope="col">Вес/Количество</th>
<th scope="col">Тип клада</th>
<th scope="col">Цена</th>
<th scope="col"></th>
</tr>
</thead>
<tbody>
{% for k, value in lib.items %}
{% for j in value %}
{% for i, p_value in am_price_lib.items %}
<tr>

<td class="align-middle">

<span><strong>{{k}}</strong>:</span>
<span>{{ j }}</span>
</td>
<td class="align-middle">
 {{i}}
</td>
<td class="align-middle">Тайник</td>
<td class="align-middle">
<span>{{ p_value }} ₽</span>
<span class="sub-price">
~{{ p_value|divide:kurs }}
<i class="fa fa-btc" aria-hidden="true"></i>
</span>
</td>
<td class="align-middle">
<span class="ttip">
<!--<i class="fa fa-info-circle" style="font-size: 18px; color: #c0c0c0; margin-right: 5px; vertical-align: middle;"></i>-->
<span class="tooltiptext">город</span>
</span>
<a href="{% url 'checkout' category BD k j i p_value %}" class="buy-button btn btn-info btn-sm">Купить</a>
</td>
</tr>
{% endfor %}
{% endfor %}
{% endfor %}

</tbody>
</table>
</div>
</div>
</div>
<section class="product-area li-laptop-product pt-30">
<div class="container">
<div class="row">
<div class="col-lg-12">
<div class="li-section-title">
<h2>
<span>Последние отзывы</span>
</h2>
</div>
<div class="col-12 mt-3 li-comment-section">
<ul>
 {% for i in coms %}
<li>
<div class="d-flex">
<div class="author-avatar pt-15">
<img src="./item_files/no-img.png" width="60" height="60" alt="">
<p class="review-operations">Покупок: {{ i.purchase }}</p>
</div>
<div class="comment-body pl-20">
<div class="d-flex align-items-center justify-content-between">
<h5 class="comment-author pt-15">{{ i.nick_name }}</h5>
<p class="pt-15 ml-3">{{ i.city }}</p>
</div>
<div class="comment-post-date">{{ i.data }}</div>
<p>{{ i.comment_text }}</p>
</div>
</div>
</li>
{% endfor %}
</ul>
</div>
</div>
</div>
</div>
</section>
</div>
</div>
</div>

</div>


{% endautoescape %}{% include "footer.html" %}