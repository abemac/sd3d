import { Component,Inject } from '@angular/core';
import {MatDialog, MatDialogRef, MAT_DIALOG_DATA} from '@angular/material';
@Component({
    selector: 'diagnostics-dialog',
    templateUrl: './diagnostics.component.html',
    styleUrls: ['./diagnostics.component.css']
  })
  export class DiagnosticsDialog {
  
    constructor(
      public dialogRef: MatDialogRef<DiagnosticsDialog>,
      @Inject(MAT_DIALOG_DATA) public data: any) { }
  
    onNoClick(): void {
      this.dialogRef.close();
    }
  
  }
  