<template>
  <div class="container">
    <div class="card logs-list">
      <div class="card-body">
        <h1 class="card-title">Logs List</h1>
        <table class="table">
          <thead>
          <tr>
            <th scope="col">ID</th>
            <th scope="col">Timestamp</th>
            <th scope="col">Level</th>
            <th scope="col">Message</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="log in paginatedLogs" :key="log.id">
            <td>{{ log.id }}</td>
            <td>{{ log.timestamp }}</td>
            <td>{{ log.level }}</td>
            <td>{{ log.message }}</td>
          </tr>
          </tbody>
        </table>
        <nav aria-label="Page navigation example">
          <ul class="pagination">
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
  name: 'LogsList',
  data() {
    return {
      logs: [],
      currentPage: 1,
      logsPerPage: 6,
    }
  },
  computed: {
    numberOfPages() {
      return Math.ceil(this.logs.length / this.logsPerPage);
    },
    paginatedLogs() {
      const start = (this.currentPage - 1) * this.logsPerPage;
      const end = start + this.logsPerPage;
      return this.logs.slice(start, end);
    },
  },
  async mounted() {
    await this.fetchLogs();
  },
  methods: {
    async fetchLogs() {
      const response = await fetch('http://localhost:5000/applogs');
      this.logs = await response.json();
    },
    changePage(number) {
      this.currentPage = number;
    },
  },
}
</script>

<!-- styles omitted for brevity -->


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

.logs-list {
  margin-top: 70px;
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
