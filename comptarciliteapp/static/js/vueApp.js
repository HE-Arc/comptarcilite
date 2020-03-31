const url = "/listAccounts/";

let vue = new Vue({
    delimiters: ['[[', ']]', ],
    el: '#app',
    data: {
        results: [],
    },
    mounted() {
        axios.get(url).then(response => {
            this.results = response.data;
            console.log(this.results);
        });
    },
});