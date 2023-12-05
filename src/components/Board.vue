<template>
    <div>Уровень:{{ lvl }}</div>
    <div style=" margin: 7px;">Время:{{ countDown }}</div>
    <div v-if="gameOver===1">Вы прошли все уровни! Баллы:{{ countDown }}</div>
    <!-- <div class="win" v-if="gameStatus===1">Вы выиграли</div> -->
    <div class="board" :style="{width: 50*size+'px', height: 50 * size +'px'}">
      <BoardItem
        v-for="(cell, index) in cells"
        :key="cell + '-' + index"
        :icon-id="cell"
        @mousedown="mousedown(index)"
        @mouseup="mouseup(index)"
        @mousemove="go(index)"
        :selected="checkRoad(index)"
        :closed="isRoadClosed(index)"
      />
    </div>
    <div @click="reload()" class="reload">Сбросить уровень</div>
</template>
  
<script lang="ts">
import BoardItem from "@/components/BoardItem.vue";
import { defineComponent, ref } from 'vue';

  
export default defineComponent({
    name: 'Board',
    
    components: {
        BoardItem
    },

    data () {
        return {
            countDown: 500
        }
    },
    methods: {
        countDownTimer (){
            if ((this.countDown > 0)&& this.gameOver!==1) {
                setTimeout(() => {
                    this.countDown -= 1
                    this.countDownTimer()
                    
                }, 1000)
            }
        }
    },
    created () {
        this.countDownTimer()
    },
    
    setup() {
        let cells = ref([3, 1, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 3]);
        const path = ref([]);
        const size = ref(4);
        const closedPath = ref([]);
        let lvl=ref(1);
        const maxLvl=13;
        let gameStatus=ref(0);
        let gameOver=ref(0);

        const mousedown = (index) => {
            path.value = [];
            
            if (cells.value[index]&& !isRoadClosed(index)) {
                path.value.push(index as never);
            }
        }

        const start=(lvl)=>{

            if(lvl===1){
                cells.value=[1,0,0,2,0,0,0,2,1];
                size.value=3;
            }
            if(lvl===2){
                cells.value=[3,1,0,1,0,0,0,0,2,0,0,0,2,0,0,3];
                size.value=4;
            }
            if(lvl===3){
                cells.value=[1,0,0,0,0,2,1,0,4,0,0,3,5,0,0,0,0,4,0,5,2,0,0,0,3];
                size.value=5;
            }
            if(lvl===4){
                cells.value=[1,0,2,0,5,0,0,3,0,4,0,0,0,0,0,0,2,0,5,0,0,1,3,4,0];
                size.value=5;
            }
            if(lvl===5){
                cells.value=[1,0,0,0,0,0,0,0,0,0,0,0,2,0,0,3,2,4,0,1,4,0,0,0,3];
                size.value=5;
            }
            if(lvl===6){
                cells.value=[0,1,2,3,0,0,0,0,4,0,0,0,4,0,0,1,0,0,5,0,2,0,5,3,0];
                size.value=5;
            }
            if(lvl===7){
                cells.value=[0,0,0,0,0,1,4,0,4,0,2,0,0,0,0,0,1,3,0,3,0,0,0,0,2];
                size.value=5;
            }
            if(lvl===8){
                cells.value=[1,0,0,0,0,0,0,3,2,0,0,3,0,0,0,1,0,0,4,0,0,5,6,0,0,5,6,0,0,2,0,0,0,0,0,4];
                size.value=6;
            }
            if(lvl===9){
                cells.value=[1,0,3,0,0,0,2,0,0,1,2,0,0,0,0,0,0,0,5,0,4,3,0,0,0,4,6,0,0,0,0,0,0,0,5,6];
                size.value=6;
            }
            if(lvl===10){
                cells.value=[0,0,0,0,0,4,0,0,0,0,3,5,0,0,5,0,0,0,4,0,0,0,0,0,1,3,2,0,1,0,0,0,0,0,2,0];
                size.value=6;
            }
            if(lvl===11){
                cells.value=[0,0,0,0,0,0,4,0,1,0,0,0,0,3,0,0,0,4,3,2,0,7,0,0,0,0,0,0,6,0,7,5,1,0,0,0,0,0,0,0,0,0,0,0,0,0,6,5,2];
                size.value=7;
            }
            if(lvl===12){
                cells.value=[1,0,0,0,0,0,0,7,0,0,7,0,4,0,0,0,0,6,4,3,0,0,5,0,0,5,0,0,0,0,0,6,2,0,0,1,2,0,0,0,3,0,0,0,0,0,0,0,0];
                size.value=7;
            }
            if(lvl===13){
                cells.value=[1,6,0,0,0,0,2,0,0,8,0,7,8,0,0,0,7,0,6,0,0,0,0,0,0,0,0,3,0,0,0,1,2,0,0,0,0,5,0,0,4,0,5,4,0,0,3,0,0];
                size.value=7;
            }
            path.value=[];
            closedPath.value=[];
    

        }
        start(lvl.value);

        const reload=()=>{
            start(lvl.value); 
        }

      
        const mouseup = (index) => {
            if (index !== path.value[0] && cells.value[index] === cells.value[path.value[0]]) {
                closedPath.value = closedPath.value.concat(path.value);
            }
            
            path.value = [];
            checkLvl();
        }

        const checkLvl=()=>{
            let completed=true;
            cells.value.forEach((cell,index)=>{
                if(cell && !isRoadClosed(index)){
                    completed=false;
                }
            })
            if(completed){
                alert('Вы выиграли!');
                goToNextLvl()
            }
        }
        
        const goToNextLvl=()=>{
            lvl.value+=1;
            gameStatus.value=0;
            if(lvl.value>maxLvl){
                lvl.value=maxLvl;
                gameStatus.value=1;
                gameOver.value=1;
            }
            start(lvl.value);
        }


      
        const go = (index) => {
            if (path.value.length) {
                const lastIndex = path.value[path.value.length - 1];
                
                if ((Math.abs(lastIndex - index) === 1 || Math.abs(lastIndex - index) === size.value)&&!isRoadClosed(index) ) {
                path.value.push(index as never);
                }
                if(isRoadClosed(index)|| (cells.value[index] && cells.value[index]!==cells.value[path.value[0]])){
                        path.value=[];
                }

            }
        }
      
        const checkRoad = (index) => {
            return path.value.findIndex(p => p === index) > -1;
        }
      
        const isRoadClosed = (index) => {
            return closedPath.value.findIndex(p => p === index) > -1;
        }
  
        return {
            cells,
            mousedown,
            mouseup,
            go,
            path,
            checkRoad,
            isRoadClosed,
            lvl,
            reload,
            size,
            gameStatus,
            gameOver,

        }
    }
})
  
</script>
  
<style>
.board {
    display: flex;
    flex-wrap: wrap;
    width: 200px;
    height: 200px;
    margin: 20px auto;
}
.reload{
    text-decoration: underline;
    cursor: pointer;
}
/* .win{
    font-weight: 700;
} */

</style>