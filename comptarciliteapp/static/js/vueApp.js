const url = "/listAccounts/";

let vue = new Vue({
    delimiters: ['[[', ']]', ],
    el: '#app',
    data: {
        accounts: [],
        accountId: null,
        transactions: [],
        accountGet: false,
        members: [],
        memberId: null,
        memberName: "",
        membersList: [],
        total: 0,
    },
    mounted() {
        axios.get(url).then(response => {
            this.accounts = response.data;
        });
        this.getMembers();
    },
    methods: {
        getAccount: function(id) {
            axios.get('/transactions/account/' + id).then(response => {
                this.transactions = response.data;
                this.accountId = this.accounts.findIndex(account => account.id === id);
                this.accountGet = true;
                console.log(this.transactions);

                // Calculate account's total amount of money
                this.total = 0.0;
                for (let t in this.transactions) {
                    this.total += parseFloat(this.transactions[t].amount);
                }

                //Adding .00 to total if int and convert to string for display
                if(this.total - parseInt(this.total) === 0)
                    this.total += ".00";
                else
                    this.total = this.total.toString();


                console.log(this.total);
                //Adding thousand separator to account's total amount
                this.total = this.total.replace(/\B(?=(\d{3})+(?!\d))/g, "'");
                console.log(this.total);
                console.log(this.accounts[this.accountId]);
            });
        },

        getMember: function(id) {
            axios.get('/members/' + id).then(response => {
                this.members.push(response.data);
                this.memberName = "";
                console.log(this.members);
            });
        },

        getMembers: function() {
            axios.get('/members/').then(response => {
                this.membersList = response.data;
                console.log(this.membersList);
            });
        },
    },
});