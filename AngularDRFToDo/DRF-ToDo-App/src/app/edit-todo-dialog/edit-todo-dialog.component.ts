import { Component, OnInit, Input, Inject, Output, EventEmitter } from '@angular/core';

import { FormControl, FormBuilder, NgForm, FormGroup, FormsModule, Validators } from '@angular/forms';
import { MatDialog, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';

import * as $ from "jquery";

import { DjangoapiService } from './../shared/djangoapi.service';


@Component({
  selector: 'app-edit-todo-dialog',
  templateUrl: './edit-todo-dialog.component.html',
  styleUrls: ['./../todos/todos.component.scss'],

  providers: [DjangoapiService],
})
export class EditTodoDialogComponent implements OnInit {

    alltodos = [{todo_title: "A", todo_status: false}, {todo_title: "B", todo_status: false}];
    showValiidationErrors: boolean;


    minDate = new Date(2021, 11, 30);
    maxDate = new Date(2022, 12, 31);


    @Output() editClicked: EventEmitter<void> = new EventEmitter();
    

    constructor(
        private djangoapi: DjangoapiService,
        public dialogRef: MatDialogRef<EditTodoDialogComponent>,
        private dialog: MatDialog,
        @Inject(MAT_DIALOG_DATA) public todo: any
    ) { }

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
    }

    close() {
        this.dialogRef.close();
    }

    onEditClicked(todo: any, form: NgForm) {

        if (form.invalid) 
            return this.showValiidationErrors = true;

        const updated_params = {
            id: todo.id,
            todo_title: form.value.todo_title,
            start_date: form.value.start_date,
            end_date: form.value.end_date,
        }

        this.djangoapi.updateSelectedToDo(updated_params).subscribe(
            data => {
                console.log("ToDo updated successfully!!!");
                window.alert("ToDo updated successfully!!!");
                window.location.reload();
            },
            error => {
                console.log(error);
                window.alert("Something went wrong!!!");
                window.location.reload();
            }
        );

        form.reset();
    }

}
