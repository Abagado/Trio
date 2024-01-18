<template>
    <div :class="
        'board-item ' 
        + (selected ? 'selected ' : '') 
        + (closed ? ' closed' : '')
    ">
        <i v-if="iconId" :class="'icon icon-'+iconId"></i>
    </div>
</template>
  
<script lang="ts">
  
    export default {
        name: 'BoardItem',

        props: {
            iconId: {
            type: Number,
            required: false,
            default: 0,
            },
            selected: {
            type: Boolean,
            required: false,
            default: false,
            },
            closed: {
            type: Boolean,
            required: false,
            default: false,
            }
        }
    }
  
</script>
  
<style>
.board-item {
    border: 1px solid #2c3e50;
    width: 48px;
    height: 48px;
    position: relative;
}

.selected {
    background-color: #00ff0083;
}

.closed {
    background-color: #00ff0050;
}
.icon{
    position: absolute;
    top:0;
    left:0;
    right: 0;
    bottom: 0;
}
.icon-1,
.icon-2,
.icon-3,
.icon-4,
.icon-5,
.icon-6,
.icon-7,
.icon-8,
.icon-9{
    background: url('../assets/icons.png');
    background-size: 150px 150px;
}

.icon-1{
    background-position: 0 0;
}
.icon-2{
    background-position: 50px 0;
}
.icon-3{
    background-position: 100px 0;
}
.icon-4{
    background-position:0 50px;
}
.icon-5{
    background-position: 50px 50px;
}
.icon-6{
    background-position: 100px 50px;
}
.icon-7{
    background-position:  100px;
}
.icon-8{
    background-position: 50px 100px;
}
.icon-9{
    background-position: 100px 100px;
}
</style>