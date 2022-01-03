import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

import { first } from 'rxjs/operators';
import { FormControl, FormBuilder, NgForm, FormGroup, FormsModule, Validators } from '@angular/forms';

import { MatDialog, MatDialogRef } from '@angular/material/dialog';
import * as $ from "jquery";

import { DjangoapiService } from './../shared/djangoapi.service';
import { ToDo } from './../shared/todo.model';
import { EditTodoDialogComponent } from './../edit-todo-dialog/edit-todo-dialog.component';



@Component({
  selector: 'app-todos',
  templateUrl: './todos.component.html',
  styleUrls: ['./todos.component.scss'],

  providers: [DjangoapiService],
})
export class TodosComponent implements OnInit {

    @Output() todoClicked: EventEmitter<void> = new EventEmitter();
    @Output() editClicked: EventEmitter<void> = new EventEmitter();
    @Output() deleteClicked: EventEmitter<void> = new EventEmitter();

	alltodos = [{todo_title: "A", todo_status: false}, {todo_title: "B", todo_status: false}];

	showValiidationErrors: boolean;

    minDate = new Date(2021, 11, 30);
    maxDate = new Date(2022, 12, 31);


  	constructor(private djangoapi: DjangoapiService, private dialog: MatDialog) {
        this.getToDos();

        console.log(this.getToDos());
    }

    getToDos = () => {
        this.djangoapi.getAllToDosfromDjango().subscribe(
            data => {
                this.alltodos = data.data.alltodos;
            },
            error => {
                console.log(error);
            }
        )
    };

  	ngOnInit(): void {
  		this.djangoapi.getAllToDosfromDjango().subscribe(
            data => {
                this.alltodos = data.data.alltodos;
            },
            error => {
                console.log(error);
            }
        )
  	}

  	onFormSubmit(form: NgForm) {
  		if (form.invalid) 
            return this.showValiidationErrors = true;

        this.createToDo(form.value);
        form.reset();
    }

    createToDo = (todo_params) => {
        this.djangoapi.createToDo(todo_params).subscribe(
            data => {
            	this.showValiidationErrors = false;
                this.getToDos();
                console.log("ToDo Record Added Successfully...");
                window.alert("Todo Created Successfully...");
            },
            error => {
                console.log(error);
                window.alert("Something went wrong!!!");
            }
        );
    };

}


    

    
