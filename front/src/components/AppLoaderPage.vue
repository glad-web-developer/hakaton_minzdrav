<template>
  <v-card class="w-100 bg-fon d-flex justify-content-center loader border-radius-0 text-center" color="blue">
    <div class="align-self-center ">
      <v-card class="px-1 py-3 card-loader">
        <div class="row">
          <div class="col-12">
            <h4>МИС Главного врача</h4>
          </div>

          <div class="col-12 my-4">
            <v-progress-circular
                :size="80"
                color="primary"
                indeterminate
            ></v-progress-circular>

          </div>
          <div class="col-12">
            <p ><b>Загрузка...</b></p>

<!--            <div class=" h3 mt-1 small">- обычно не дольше 10 секунд</div>-->
<!--            <div class="h3 mt-1 small">- если дольше, то обновите страничку</div>-->
<!--            <div class=" h3 mt-1 small">- если не помогло, то звоните в тех. поддержку</div>-->
          </div>
        </div>


      </v-card>
    </div>
  </v-card>
</template>

<script>
export default {
  name: "AppLoaderPage"
}
</script>

<style scoped>
.loader {
  height: 100vh;
}

.card-loader{
  width: 300px;
}

.bg-fon{
  background-image: url("../assets/fon.jpg");
  background-size: cover;
}

.fadeIn {
  -webkit-animation-name: fadeIn;
  animation-name: fadeIn;
  -webkit-animation-duration: 1s;
  animation-duration: 1s;
  -webkit-animation-fill-mode: both;
  animation-fill-mode: both;
  animation-iteration-count: infinite;
}

@-webkit-keyframes fadeIn {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }

}

@keyframes fadeIn {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}
</style>