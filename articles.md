---
layout: inner
permalink: /articles/
---
<ul class="blog-list">
  {% for post in site.data.medium_posts %}
  <li>
    <a href="{{ post.url }}" target="_blank" rel="noopener noreferrer">
      <img src="{{ post.thumbnail }}" alt="{{ post.title }}" />
      <div>
        <h3>{{ post.title }}</h3>
        <time datetime="{{ post.date }}">{{ post.date | date: "%B %e, %Y" }}</time>
        <p>{{ post.excerpt }}</p>
      </div>
    </a>
  </li>
  {% endfor %}
</ul>