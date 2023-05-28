import Vue from 'vue'
import Vuex from 'vuex'
import {AuthModule, UserModule} from "@/entities/user/model";
import {ProtocolModule} from "@/entities/protocol/model";
import {PatientModule} from "@/entities/patient/model";

Vue.use(Vuex)

export default new Vuex.Store({
    modules: {
        user: UserModule,
        auth: AuthModule,
        protocol: ProtocolModule,
        patient: PatientModule,
    }
})

