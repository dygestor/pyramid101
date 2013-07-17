<%inherit file="default.mako" />
<%block name="title">Prihlasenie</%block>
<%block name="page_content">
% for user in users:
    <div> ${user.id} with email ${user.email} and name ${user.name} <a href="/delete/${user.id}">Zmazat</a></div>
% endfor
</%block>
