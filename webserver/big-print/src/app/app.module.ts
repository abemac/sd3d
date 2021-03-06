import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';


import { AppComponent } from './app.component';
import {CreateDialog} from './create/create.component'
import {AboutDialog} from './about/about.component'
import {DiagnosticsDialog} from './diagnostics/diagnostics.component'
import {ViewDialog} from './view/view.component'
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {MatCardModule,MatGridListModule,MatDialogModule,
  MatButtonModule,MatStepperModule,MatFormFieldModule,
  MatInputModule
} from '@angular/material'

import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import {FileUploadModule} from 'ng2-file-upload'
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,CreateDialog,AboutDialog,DiagnosticsDialog,ViewDialog
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    MatCardModule,
    MatGridListModule,
    MatDialogModule,
    MatButtonModule,
    MatStepperModule,
    FormsModule,
    ReactiveFormsModule,
    MatFormFieldModule,
    MatInputModule,
    FileUploadModule,
    HttpClientModule
    
  ],
  entryComponents: [
    CreateDialog,AboutDialog,DiagnosticsDialog,ViewDialog
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
