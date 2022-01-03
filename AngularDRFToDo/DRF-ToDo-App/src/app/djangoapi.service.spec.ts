import { TestBed } from '@angular/core/testing';

import { DjangoapiService } from './djangoapi.service';


describe('DjangoapiService', () => {
    let service: DjangoapiService;

    beforeEach(() => {
        TestBed.configureTestingModule({});
        service = TestBed.inject(DjangoapiService);
    });

    it('should be created', () => {
        expect(service).toBeTruthy();
    });
});
