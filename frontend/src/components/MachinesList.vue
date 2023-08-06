<template>


    <div class="container">
        <div class="card machines-list">
            <div class="card-body">
                <h1 class="card-title">Machines List</h1>
                <table class="table">
                    <thead>
                    <tr>
                        <th scope="col">ID</th>
                        <th scope="col">Model</th>
                        <th scope="col">Location</th>
                        <th scope="col">Care Taker</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for="machine in paginatedData" :key="machine.id">
                        <td>{{ machine.id }}</td>
                        <td>{{ machine.model }}</td>
                        <td>{{ machine.location_id }}</td>
                        <td>{{ machine.caretaker_id }}</td>
                    </tr>
                    </tbody>

                </table>
                <nav aria-label="Page navigation example">
                    <ul class="pagination">
                        <li>
                            <button @click="sortMachines" class="btn btn-outline-primary">Sort by ID</button>
                        </li>
                        <li class="page-item"
                            v-for="number in numberOfPages"
                            :key="number"
                            :class="{'active': number === currentPage}">
                            <a class="page-link" href="#" @click.prevent="changePage(number)">{{ number }}</a>

                        </li>
                    </ul>
                </nav>
            </div>
        </div>
    </div>
</template>


<script>
import axios from 'axios';

export default {
    data() {
        return {
            coffeeMachines: [],
            currentPage: 1,
            itemsPerPage: 10,
            sortAsc: true,

        };
    },
    computed: {

        paginatedData() {
            const start = (this.currentPage - 1) * this.itemsPerPage;
            const end = this.currentPage * this.itemsPerPage;
            return this.coffeeMachines.slice(start, end);
        },

        numberOfPages() {
            return Math.ceil(this.coffeeMachines.length / this.itemsPerPage);
        }
    },
    methods: {
        async getCoffeeMachines() {
            try {
                const response = await axios.get('http://127.0.0.1:5000/coffee_machines');
                this.coffeeMachines = response.data.coffee_machines;
            } catch (error) {
                console.error(error);
            }
        },
        changePage(pageNumber) {
            this.currentPage = pageNumber;
        },
        sortMachines() {
    this.sortAsc = !this.sortAsc;
    this.coffeeMachines.sort((a, b) => {
        let comparison = 0;
        if (a.id > b.id) {
            comparison = 1;
        } else if (a.id < b.id) {
            comparison = -1;
        }
        return this.sortAsc ? comparison : comparison * -1;
    });
}


    },
    mounted() {
        this.getCoffeeMachines();
    },

};
</script>


<style scoped>
.container {
    background-color: #f2f2f2;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 820px;
    margin-top:45px;
    margin-left:220px;
    border-radius: 1rem;
}
.machines-list {

    margin-top: -1rem;
    border-radius: 1rem;
    width: 100%;

}

.table {
    margin-bottom: 0;
    height: 100%;


}

.table tr:nth-child(even) {
    background-color: #f2f2f2;
}

.table tr:hover {
    background-color: #dddd;


}

nav {

    margin-top: 30px;
    margin-left: 20px;


}
nav button{

    margin-right:10px;
}
</style>