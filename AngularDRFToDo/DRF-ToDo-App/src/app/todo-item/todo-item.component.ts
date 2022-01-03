import { Component, OnInit, Output, Input, EventEmitter } from '@angular/core';

import { ToDo } from './../shared/todo.model';

import { FormBuilder, NgForm, FormGroup, FormsModule, Validators } from '@angular/forms';

import { MatDialog, MatDialogRef } from '@angular/material/dialog';
import { DjangoapiService } from './../shared/djangoapi.service';

import { EditTodoDialogComponent } from './../edit-todo-dialog/edit-todo-dialog.component';
import { DeleteTodoDialogComponent } from './../delete-todo-dialog/delete-todo-dialog.component';


@Component({
  selector: 'app-todo-item',
  templateUrl: './todo-item.component.html',
  styleUrls: ['./todos.item.component.scss']
})
export class TodoItemComponent implements OnInit {

	alltodos = [{todo_title: "A", todo_status: false}, {todo_title: "B", todo_status: false}];

	@Input() todo: ToDo
	@Output() todoClicked: EventEmitter<void> = new EventEmitter();
	@Output() editClicked: EventEmitter<void> = new EventEmitter();
	@Output() deleteClicked: EventEmitter<void> = new EventEmitter();


  	constructor(private djangoapi: DjangoapiService, private dialog: MatDialog) {
        this.getToDos();
        console.log(this.getToDos());
    }

  	ngOnInit(): void {
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

  	toggleCompleted(todo: any) {
        this.todoClicked.emit();
        this.djangoapi.toggleToDoStatusCompleted(todo).subscribe(
            data => {
                this.getToDos();
                console.log("Task status has been changed.");
                window.alert("Task status has been changed.");
                window.location.reload();
            },
            error => {
                console.log(error);
                window.alert("Something went wrong!!!");
            }
        );
    }

    onEditClicked(todo: any) {
        let dialogRef = this.dialog.open(EditTodoDialogComponent, {
            width: "700px",
            data: todo
        });
    }

    onDeleteClicked(todo: any) {
        let dialogRef = this.dialog.open(DeleteTodoDialogComponent, {
            width: "700px",
            data: todo
        });
    }
    

}
