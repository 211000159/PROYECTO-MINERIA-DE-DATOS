import { Component, ViewChild } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { TextComponent } from '../../../shared/components/input/text/text.component';
import { PasswordComponent } from '../../../shared/components/input/password/password.component';
import { CaptchaComponent } from '../../../shared/components/captcha/captcha.component';


import {
  FormsModule,
  ReactiveFormsModule,
  FormGroup,
  FormBuilder,
  Validators,
} from '@angular/forms';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [
    ReactiveFormsModule, TextComponent,
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    RouterModule,
    TextComponent,
    PasswordComponent,
    CaptchaComponent,
  ],
  templateUrl: './login.component.html',
  styleUrl: './login.component.scss',
})
export class LoginComponent {
  submitted = false;
  loginForm: FormGroup;

  constructor(private fb: FormBuilder) {
    this.loginForm = this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required]],
    });
  }

  @ViewChild(CaptchaComponent) captchaComponent!: CaptchaComponent; 

  get email() {
    return this.loginForm.get('email');
  }

  get password() {
    return this.loginForm.get('password');
  }

  getEmailErrorMessage(): string {
    const emailControl = this.email;
    if (
      emailControl &&
      (emailControl?.touched || emailControl?.dirty || this.submitted == true)
    ) {
      if (emailControl.hasError('required')) {
        return 'Email is required.';
      }

      if (emailControl.hasError('email')) {
        return 'Please enter a valid email address.';
      }
    }
    return '';
  }

  getPassErrorMessage(): string {
    const passControl = this.password;
    if (
      passControl &&
      (passControl?.touched || passControl?.dirty || this.submitted == true)
    ) {
      if (passControl.hasError('required')) {
        return 'Password is required.';
      }
    }
    return '';
  }

  handleCaptchaVerification(isVerified: boolean) {
    if (isVerified) {
      console.log('CAPTCHA is verified!');
    } else {
      console.log('CAPTCHA verification failed.');
    }
  }

  handleVerfitication() {
   
    this.getEmailErrorMessage();
    this.getPassErrorMessage();
  }

  onSubmit() {
    this.submitted = true;
    this.handleVerfitication();
  }
}