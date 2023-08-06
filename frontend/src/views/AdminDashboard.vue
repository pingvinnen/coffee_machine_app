<template>
  <div id="admin-dashboard">
    <AppNavbar />
    <SideBar />
    <MachinesList/>
  </div>
</template>

<script>
import AppNavbar from '@/components/AppNavbar.vue';
import SideBar from "@/components/SideBar.vue";
import MachinesList from "@/components/MachinesList.vue";

export default {
    components: {
        MachinesList,
        AppNavbar,
        SideBar,
    },
    data() {
        return {

        }

    }
};
</script>

<style scoped>
#admin-dashboard {
  display: grid;
  grid-template-columns: 250px 1fr;
  grid-template-rows: auto 1fr;
  height: 100vh;
}


#admin-dashboard > :first-child {
  grid-column: 1 / -1;
}


#admin-dashboard > :nth-child(2) {
  grid-row: 2;
}


#admin-dashboard > :last-child {
  grid-column: 2;
  grid-row: 2;
}
</style>
