class KeyBoard {

    constructor(domElementId, textInputId) {
        this.keyboard = document.getElementById(domElementId);
        this.input = document.getElementById(textInputId);

        this.mapStdKeys = [
            '1234567890+',
            'qwertyuiopå¨',
            'asdfghjklöä',
            '<zxcvbnm,.-'
        ];
        this.mapShiftKeys = [
            '!"#¤%&/()=?',
            'QWERTYUIOPÅ^',
            'ASDFGHJKLÖÄ',
            '>ZXCVBNM;:_'
        ];
        this.mapAltGrKeys = [
            '¡@£$€¥{[]}\'',
            '@ł€®þ←↓→œþ',
            'ªßðđŋħłøæ´',
            '|«»©“”nµ̣¸·̣̣̣'
        ];

        domElementId, textInputId

        this.STD_KEYS = 0;
        this.SHIFT_KEYS = 1;
        this.ALTGR_KEYS = 2;
        this.currentKeyboard = 0;

        this.stdKeys = this.createKeyboard(this.STD_KEYS, this.mapStdKeys);
        this.shiftKeys = this.createKeyboard(this.SHIFT_KEYS, this.mapShiftKeys);
        this.altGrKeys = this.createKeyboard(this.ALTGR_KEYS, this.mapAltGrKeys);

        this.addExtraButtons(this.keyboard);
        this.show();
    }

    update() {
        hide(this.stdKeys);
        hide(this.shiftKeys);
        hide(this.altGrKeys);

        switch (this.currentKeyboard) {
            case this.STD_KEYS:
                show(this.stdKeys);
                return;
            case this.SHIFT_KEYS:
                show(this.shiftKeys);
                return;
            case this.ALTGR_KEYS:
                show(this.altGrKeys);
                return;
        }
    }

    hide() {
        hide(this.keyboard);
    }

    show() {
        show(this.keyboard);
        this.update();
    }

    addExtraButtons(keyboard) {
        keyboard.appendChild(this.createKey('shift'));
        keyboard.appendChild(this.createKey('Alt Gr'));
        keyboard.appendChild(this.createKey('space'));
        //keyboard.appendChild(this.createKey('return'));
        keyboard.appendChild(this.createKey('back'));
        keyboard.appendChild(this.createKey('clear'));
    }

    createKeyboard(id, keymap) {
        let keyboard = document.createElement('div');
        keyboard.classList.add('keyboard');
        keyboard.classList.add('hidden');
        keyboard.id = 'keyboard-' + id;

        for (let keyRow of keymap) {
            let row = this.createRow();
            for (let key of keyRow) {
                row.appendChild(this.createKey(key));
            }
            keyboard.appendChild(row);
        }

        this.keyboard.appendChild(keyboard);
        return keyboard;
    }

    createRow() {
        let rowDiv = document.createElement('div');
        rowDiv.classList.add('key-row');
        return rowDiv;
    }

    createKey(name) {
        let key = document.createElement('button');
        key.id = 'key-' + name;
        key.innerHTML = name;
        key.classList.add('key');
        key.addEventListener('click', () => this.keyPress(name));
        return key;
    }

    keyPress(key) {

        switch (key) {
            case 'shift':
                if (keyBoard.currentKeyboard == keyBoard.SHIFT_KEYS)
                    keyBoard.currentKeyboard = keyBoard.STD_KEYS;
                else
                    keyBoard.currentKeyboard = keyBoard.SHIFT_KEYS;
                this.update();
                break;
            case 'Alt Gr':
                if (keyBoard.currentKeyboard == keyBoard.ALTGR_KEYS)
                    keyBoard.currentKeyboard = keyBoard.STD_KEYS;
                else
                    keyBoard.currentKeyboard = keyBoard.ALTGR_KEYS;
                this.update();
                break;
            case 'space':
                this.input.value += ' ';
                break;
            case 'back':
                this.input.value = this.input.value.substr(0, this.input.value.length-1);
                break;
            case 'clear':
                this.input.value = '';
                break;
            case 'return':
                console.log('SEND')
                break;
            default:
                this.input.value += key;
        }
    }

    read() {
        return this.input.value;
    }
}