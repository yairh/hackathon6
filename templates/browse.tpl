<h1>Browse the available skills</h1>
<div class="browse">
% for skill in result:
    <article class="clickable shadowed" onclick="Browse.loadShow('{{skill[0]}}')">
        <div class="cover-holder">
            <img src="{{skill[2]}}" class="show-cover"/>
        </div>
        <h3 class="show-name">{{skill[1]}}</h3>
    </article>
% end
</div>

