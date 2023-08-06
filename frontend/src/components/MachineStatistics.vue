
<template>

  <head>

    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" rel="stylesheet">
  </head>


  <div class="app-container">
    <AppNavbar/>
    <div class="row">
      <div class="col-3">

        <SideBar/>
      </div>
      <div class="col-9">
        <div class="container">
          <div class="row">
            <div class="col-lg-4 col-md-6" style="margin-top: 20px">
              <div class="card border-primary">
                <div class="card-body bg-primary text-white">
                  <div class="row">
                    <div class="col-3">
                     <i class="fas fa-coffee text-white fa-5x"></i>
                    </div>
                    <div class="col-9 text-right">
                      <h1>{{ totalCoffeeMachines }}</h1>
                      <h4>Total Coffee Machines</h4>
                    </div>
                  </div>
                </div>
                <a href=" " target="_blank">
                  <div class="card-footer bg-light text-primary">
                    <span class="float-left">More details</span>
                    <span class="float-right"><i class="fa fa-arrow-circle-right"></i></span>
                    <div class="clearfix"></div>
                  </div>
                </a>
              </div>
            </div>
            <div class="col-lg-4 col-md-6" style="margin-top: 20px">
              <div class="card border-secondary">
                <div class="card-body bg-secondary text-white">
                  <div class="row">
                    <div class="col-3">
                      <i class="fas fa-arrow-up text-white fa-5x "></i>
                    </div>
                    <div class="col-9 text-right">
                      <h1>{{ totalCoffeMachinesUp }}</h1>
                      <h4>Total Coffee Machines Up</h4>
                    </div>
                  </div>
                </div>
                <a href=" " target="_blank">
                  <div class="card-footer bg-light text-secondary">
                    <span class="float-left">More details</span>
                    <span class="float-right"><i class="fa fa-arrow-circle-right"></i></span>
                    <div class="clearfix"></div>
                  </div>
                </a>
              </div>
            </div>
            <div class="col-lg-4 col-md-6" style="margin-top: 20px">
              <div class="card border-success">
                <div class="card-body bg-success text-white">
                  <div class="row">
                    <div class="col-3">
                      <i class="fas fa-arrow-down text-white fa-5x"></i>
                    </div>
                    <div class="col-9 text-right">
                      <h1>{{ TotalMachinesDown }}</h1>
                      <h4>Total Machines Down</h4>
                    </div>
                  </div>
                </div>
                <a href=" " target="_blank">
                  <div class="card-footer bg-light text-success">
                    <span class="float-left">More details</span>
                    <span class="float-right"><i class="fa fa-arrow-circle-right"></i></span>
                    <div class="clearfix"></div>
                  </div>
                </a>
              </div>
            </div>
            <div class="col-lg-4 col-md-6" style="margin-top: 20px">
              <div class="card border-danger">
                <div class="card-body bg-danger text-white">
                  <div class="row">
                    <div class="col-3">
                     <i class="fas fa-file text-white fa-5x"></i>
                    </div>
                    <div class="col-9 text-right">
                      <h1>{{ TotalIncidents }}</h1>
                      <h4>Application Incidents This Month</h4>
                    </div>
                  </div>
                </div>
                <a href="/applogs " target="_blank">
                  <div class="card-footer bg-light text-danger">
                    <span class="float-left">More details</span>
                    <span class="float-right"><i class="fa fa-arrow-circle-right"></i></span>
                    <div class="clearfix"></div>
                  </div>
                </a>
              </div>
            </div>
            <div class="col-lg-4 col-md-6" style="margin-top: 20px">
              <div class="card border-warning">
                <div class="card-body bg-warning text-white">
                  <div class="row">
                    <div class="col-3">
                      <i class="fas fa-exclamation text-white fa-5x"></i>
                    </div>
                    <div class="col-9 text-right">
                      <h1>{{ TotalWarnings }}</h1>
                      <h4>Warnings This Month</h4>
                    </div>
                  </div>
                </div>
                <a href=" " target="_blank">
                  <div class="card-footer bg-light text-warning">
                    <span class="float-left">More details</span>
                    <span class="float-right"><i class="fa fa-arrow-circle-right"></i></span>
                    <div class="clearfix"></div>
                  </div>
                </a>
              </div>
            </div>
            <div class="col-lg-4 col-md-6" style="margin-top: 20px">
              <div class="card border-info">
                <div class="card-body bg-info text-white">
                  <div class="row">
                    <div class="col-3">
                      <i class="fas fa-check text-white fa-5x"></i>
                    </div>
                    <div class="col-9 text-right">
                      <h1>{{ SolvedThisMont }}</h1>
                      <h4>Solved This Month</h4>
                    </div>
                  </div>
                </div>
                <a href=" " target="_blank">
                  <div class="card-footer bg-light text-info">
                    <span class="float-left">More details</span>
                    <span class="float-right"><i class="fa fa-arrow-circle-right"></i></span>
                    <div class="clearfix"></div>
                  </div>
                </a>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>

</template>

<script>
import AppNavbar from "@/components/AppNavbar.vue";
import SideBar from "@/components/SideBar.vue";

export default {
  components: {
    SideBar,
    AppNavbar,
  },
  data() {
    return {
      totalCoffeeMachines: 75,
      totalCoffeMachinesUp: 10,
      TotalMachinesDown: 8,
      TotalIncidents: 2,
      TotalWarnings: 4,
      SolvedThisMont: 17,
    };
  },
};
</script>


<style scoped>
.app-container {
    overflow-x: hidden;
}


.container {
  margin-top: 100px;
  margin-left:0px
}
.sidebar {
    height: 100vh;
    width:250px;
}
a {

  text-decoration: none;
}


</style>