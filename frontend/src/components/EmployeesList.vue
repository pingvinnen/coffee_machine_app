<template>
  <div class="container">
    <div class="card employees-list">
      <div class="card-body">
        <h1 class="card-title">Employees List</h1>
        <table class="table">
          <thead>
          <tr>
            <th scope="col">ID</th>
            <th scope="col">Name</th>
            <th scope="col">Title ID</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="employee in employees" :key="employee.id">
            <td>{{ employee.id }}</td>
            <td>{{ employee.name }}</td>
            <td>{{ employee.role}}</td>
          </tr>
          </tbody>

        </table>
        <nav aria-label="Page navigation example">
          <ul class="pagination">
            <li>
              <button @click="sortEmployees" class="btn btn-outline-primary">Sort by ID</button>
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
export default {
  name: 'EmployeesList',
  data() {
    return {
      employees: [],
    }
  },
  async mounted() {
    await this.fetchEmployees();
  },
  methods: {
    async fetchEmployees() {
      const response = await fetch('http://localhost:5000/employees');
      this.employees = await response.json();
    }
  }
}
</script>

<style scoped>
.container {
  background-color: #f2f2f2;
  justify-content: center;
  align-items: center;
  height: 820px;
  margin-top: 45px;
  margin-left: 220px;
  border-radius: 1rem;
}

.card-body {
  padding: 50px;
  border-radius: 1rem;
  width: 100%;
}
.employees-list{
  margin-top:70px;


}
.table {
  margin-bottom: 0;
  height: 100%;
  width: 100%;
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

nav button {
  margin-right: 10px;
}
</style>
