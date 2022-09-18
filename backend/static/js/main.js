  // Get Search form and page links
  let searchForm = document.querySelector('#searchForm');
  let pageLinks = document.getElementsByClassName('page-link')

  // Ensure  search form exists

  if (searchForm){

    for(let i = 0; i < pageLinks.length; i++) {
        pageLinks[i].addEventListener('click', function(e){
            e.preventDefault();
            
            // Get the data attribute
            let page = this.dataset.page;

            // Add hidden search input to form 
            searchForm.innerHTML += `<input type="hidden" name="page" value="${page}" />`;

            // Submit form
            searchForm.submit();
        });
    }

  }

let tags = document.getElementsByClassName('project-tag')
for (let i = 0; i < tags.length; i++ ){
    tags[i].addEventListener('click', (e) => {
        let tagId = e.target.dataset.tag
        let projectId = e.target.dataset.project

        fetch("http://127.0.0.1:8000/api/delete-tag/", {
            method: "DELETE",
            headers: {
                'Content-Type': "application/json "
            },
            body: JSON.stringify({
                "tagId": tagId,
                "projectId": projectId,
        })
        }) .then(response => response.json())
        .then(data => {
            e.target.remove()
        })
})
}