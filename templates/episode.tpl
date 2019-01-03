<h1>{{nameOfSkill}}</h1>

<br>
<ul class="skillers-results">
% for people in result:
<li class="people-results" >{{people[1]}}</li>
% end
% if not result:
    No Results :(
% end

</ul>