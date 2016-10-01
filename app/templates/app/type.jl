type {{ name.title() }}

  {% for field in fields %}
    {{- field }}
  {% endfor %}
end
