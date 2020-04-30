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
        withdrawal: 0,
        deposit: 0,
        description: "",
        timestamp: "",
        transactionSuccess: null,
        transactionMessage: "",
        accountDbId: 0,
    },
    mounted() {
        axios.get(url).then(response => {
            this.accounts = response.data;
        });
        this.getMembers();
        this.timestamp = this.getFormattedDate(new Date(Date.now()));
    },
    methods: {
        getAccount: function(id) {
            axios.get('/transactions/account/' + id).then(response => {
                this.transactions = response.data;
                this.accountId = this.accounts.findIndex(account => account.id === id);
                this.accountDbId = id;
                this.accountGet = true;

                // Calculate account's total amount of money
                this.total = 0.0;
                for (let t in this.transactions) {
                    this.total += parseFloat(this.transactions[t].amount);
                }

                //Adding .00 to total if int and convert to string for display
                if (this.total - parseInt(this.total) === 0)
                    this.total += ".00";
                else
                    this.total = this.total.toString();


                //Adding thousand separator to account's total amount
                this.total = this.total.replace(/\B(?=(\d{3})+(?!\d))/g, "'");
            });
        },

        getMember: function(id) {
            axios.get('/members/' + id).then(response => {
                this.members.push(response.data);
                this.memberName = "";
            });
        },

        getMembers: function() {
            axios.get('/members/').then(response => {
                this.membersList = response.data;
            });
        },
        addTransaction: function() {
            let csrf_token = "";
            data = {
                "timestamp": new Date(Date.parse(this.timestamp)).toJSON(),
                "description": this.description,
                "user": this.user,
                "account": this.accountDbId,
            };
            if (this.withdrawal > 0) {
                data["amount"] = -this.withdrawal;
            } else if (this.deposit > 0) {
                data["amount"] = this.deposit;
            } else {
                this.transactionSuccess = false;
                this.transactionMessage = "Vous devez ajouter un montant !";
                return;
            }
            axios.get('/csrf_token/')
                .then(response => {
                    csrf_token = response.data["token"];
                    axios.post('/transactions/', data, {
                            headers: {
                                'X-CSRFToken': csrf_token,
                            },
                        })
                        .then(response => {
                            this.transactionSuccess = true;
                            this.transactionMessage = "Transaction ajouté avec succès";
                            this.getAccount(this.accountDbId);
                            this.description = "";
                            this.withdrawal = 0;
                            this.deposit = 0;
                        })
                        .catch(error => {
                            this.transactionSuccess = false;
                            this.transactionMessage = error;
                        });
                })

        },
        getFormattedDate: function(date) {
            dateType = new Date(Date.parse(date));
            return dateType.getFullYear() + "-" + (dateType.getMonth() + 1).toString() + "-" + dateType.getDate() + " " + dateType.getHours() + ":" + dateType.getMinutes();
        },
    },
});