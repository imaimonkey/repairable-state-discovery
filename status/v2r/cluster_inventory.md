# V2R cluster inventory

2026-09-24T11:24:27.523083+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324352106496 available bytes; 81.91% used; 112488881 free inodes.

server1 `/home`: 324352106496 available bytes; 81.91% used; 112488881 free inodes.

server1 `/tmp`: 324352106496 available bytes; 81.91% used; 112488881 free inodes.

server1 `/var/tmp`: 324352106496 available bytes; 81.91% used; 112488881 free inodes.

server1 `/mnt/raid5`: 454198276096 available bytes; 97.92% used; 337690243 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 57670434816 available bytes; 96.78% used; 110430056 free inodes.

server2 `/home`: 57670434816 available bytes; 96.78% used; 110430056 free inodes.

server2 `/tmp`: 57670434816 available bytes; 96.78% used; 110430056 free inodes.

server2 `/var/tmp`: 57670434816 available bytes; 96.78% used; 110430056 free inodes.

server2 `/mnt/raid5`: 510807904256 available bytes; 96.47% used; 445173461 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85742727168 available bytes; 95.22% used; 114196377 free inodes.

server3 `/home`: 85742727168 available bytes; 95.22% used; 114196377 free inodes.

server3 `/data`: 144884518912 available bytes; 98.00% used; 225816755 free inodes.

server3 `/tmp`: 85742727168 available bytes; 95.22% used; 114196377 free inodes.

server3 `/var/tmp`: 85742727168 available bytes; 95.22% used; 114196377 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105731092480 available bytes; 94.10% used; 114348877 free inodes.

server4 `/home`: 105731092480 available bytes; 94.10% used; 114348877 free inodes.

server4 `/data`: 115640868864 available bytes; 98.40% used; 225258075 free inodes.

server4 `/tmp`: 105731092480 available bytes; 94.10% used; 114348877 free inodes.

server4 `/var/tmp`: 105731092480 available bytes; 94.10% used; 114348877 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
