function search(){
    if(DocumentFragment.getElementById(search_input).value!="") {
        window.location.href="{% url 'GlaCine:login' %}" +document.getElementById(search_input).value;
        document.getElementById(search_input).value = "";
    }
    return false;
}