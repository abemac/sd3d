import { Component,Inject,OnInit } from '@angular/core';
import {MatDialog, MatDialogRef, MAT_DIALOG_DATA} from '@angular/material';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import { FileUploader } from 'ng2-file-upload';

const URL = 'https://bigprint.technology/api';

@Component({
    selector: 'create-dialog',
    templateUrl: './create.component.html',
    styleUrls: ['./create.component.css']
  })
  export class CreateDialog implements OnInit{
    isLinear = false;
    firstFormGroup: FormGroup;
    secondFormGroup: FormGroup;

    public uploader:FileUploader = new FileUploader({url: URL});
    public hasBaseDropZoneOver:boolean = false;
    public hasAnotherDropZoneOver:boolean = false;
   
    public fileOverBase(e:any):void {
      this.hasBaseDropZoneOver = e;
    }

    constructor(
      public dialogRef: MatDialogRef<CreateDialog>,
      @Inject(MAT_DIALOG_DATA) public data: any,
      private formBuilder: FormBuilder) { }
  
    ngOnInit() {
      this.firstFormGroup = this.formBuilder.group({
        firstCtrl: ['', Validators.required]
      });
      this.secondFormGroup = this.formBuilder.group({
        secondCtrl: ['', Validators.required]
      });
    }
  
  }
  