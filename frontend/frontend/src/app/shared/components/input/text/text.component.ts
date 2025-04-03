import { Component, Input } from '@angular/core';

@Component({
  selector: 'global-input-text',
  standalone: true,
  imports: [],
  templateUrl: './text.component.html',
  styleUrl: './text.component.scss',
})
export class TextComponent {
  @Input({ required: true }) name!: string;
  @Input() icon: string = 'mail_outline';
  @Input() type: string = 'text';
  @Input() label: string = '';
  @Input() placeholder: string = '';
  @Input() required: boolean = false;
  @Input() inputClass: string = '';
  @Input() labelClass: string = 'w-full form-control';
}