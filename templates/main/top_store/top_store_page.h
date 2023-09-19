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
<a href="{% url 'stores' %}">
Магазины
</a>
</li>
<li>
<a class="active">
 {{store.name}}
</a>
</li>
</ul>
</div>
</div>
</div>
<div class="content-wraper pt-30 pb-60">
<div class="container">

<div>
<div class="shop-banner">
 {% if store.cover %}
 <img class="w-100" src="{{ store.cover.url }}" alt="" style="border-radius: 3px;">
{% else %}
<img class="w-100" src="static/images/no-cover.png" alt="" style="border-radius: 3px;">
 {% endif %}
</div>
<div class="d-flex justify-content-sm-between flex-wrap p-3 pb-1 pt-4">
<div class="d-flex align-items-center">
 <span style="font-size: 20px;">&#128081;</span>

<h5 class="mb-0 store-details__title">{{store.name}}</h5>
<span class="ml-25">
<span>Рейтинг: <strong>{{store.rating}}</strong></span>
</span>
<span class="ml-25">
<span>Продаж: <strong>{{store.sold}}</strong></span>
</span>
<span class="ml-25">
<span>Депозит:
<strong>{{store.deposit}}</strong> <i class="fa fa-btc"></i>
</span>
</span>
  <span class="ml-25">
<span>Категория:
<strong>{{ store.store_type }}</strong>
</span>
</span>
</div>
<a href="">
<span style="vertical-align: middle;">Написать продавцу</span>
</a>
</div>
<div class="d-flex justify-content-sm-between flex-wrap p-3" style="background-color: #f9f9f9;">
<div class="d-flex align-items-center">
<a href="{% url 'store_work' store.id %}" class="ml-25">Правила магазина</a>
<a href="{% url 'store_reviews' store.id %}" class="ml-25">Отзывы магазина</a>
<strong>
<a style="" href="{% url 'store_work' store.id %}" class="ml-25">Работа</a>
</strong>
 {% if store.forum %}
 <a href="{{ store.forum }}" class="ml-25">Форум</a>
{% endif %}
 {% if store.sales %}
 <a href="{% url 'store_sales' store.id %}" class="ml-25">Акции</a>
{% endif %}
</div>
 {% if store.telegram_bot %}
<div class="d-flex align-items-center">
<a href="{{ store.telegram_bot }}" target="_blank" class="bot-button custom-btn__orange ml-20">Telegram бот</a>
</div>
 {% endif %}
</div>
</div>
<section class="product-area li-laptop-product pt-45 pb-30">
<div class="container">
<div class="row">
<div class="col-lg-12">
<div class="li-section-title">
<h2>
<span>Витрина магазина</span>
</h2>
</div>

<div class="row mt-3">

{% for i in store_items %}
<div class="col-6 col-md-3 col-lg-2 col-sm-4 mb-30">
<a href="">
</a><div class="single-product-wrap">
 <a href="{% url 'item' i.id BD %}">


{% if i.img %}
 <div class="product-image">
<img src="{{ i.img.url }}" alt="Product Image">
</div>
 {% endif %}
</a><div class="product_desc"><a href="">
</a><div class="product_desc_info"><a href="">
<h4 class="product_name text-truncate text-center" title="{{ i.name }}">
{{ i.name }}
</h4>
</a><h4 class="product_name text-truncate text-center mt-0 pt-0"><a href="">
<img width="13px" src="./store_page_files/crown.svg" alt="">
</a><a href="">{{ i.store }}</a>
</h4>
<div class="price-box text-center">
<div class="price-line">
<span class="new-price">от <strong>{{ i.min_price }} ₽</strong> /
{{ i.amount }}
г
</span>
</div>
<span class="sub-price">
~{{ i.min_price|divide:kurs }}
<i class="fa fa-btc" aria-hidden="true"></i>
</span>
</div>
</div>
</div>
</div>

</div>
{% endfor %}



</div>
</div>
</div>
</div>
</section>
<section class="product-area li-laptop-product">
<div class="container">
<div class="row">
<div class="col-lg-12">
<div class="li-section-title">
<h2>
<span>Описание магазина</span>
</h2>
 </div>
<div class="shop-description p-3 mt-1">
<pre style="font-weight: normal;
    font-size: initial; font-family: sans-serif;">
 {{ store.description }}
</pre>
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
