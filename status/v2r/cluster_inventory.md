# V2R cluster inventory

2026-09-24T02:09:34.753734+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325446938624 available bytes; 81.84% used; 112499239 free inodes.

server1 `/home`: 325446938624 available bytes; 81.84% used; 112499239 free inodes.

server1 `/tmp`: 325446938624 available bytes; 81.84% used; 112499239 free inodes.

server1 `/var/tmp`: 325446938624 available bytes; 81.84% used; 112499239 free inodes.

server1 `/mnt/raid5`: 734709702656 available bytes; 96.63% used; 337733524 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40908369920 available bytes; 97.72% used; 110431686 free inodes.

server2 `/home`: 40908369920 available bytes; 97.72% used; 110431686 free inodes.

server2 `/tmp`: 40908369920 available bytes; 97.72% used; 110431686 free inodes.

server2 `/var/tmp`: 40908369920 available bytes; 97.72% used; 110431686 free inodes.

server2 `/mnt/raid5`: 529648259072 available bytes; 96.34% used; 445200258 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292685537280 available bytes; 83.67% used; 114210523 free inodes.

server3 `/home`: 292685537280 available bytes; 83.67% used; 114210523 free inodes.

server3 `/data`: 56778833920 available bytes; 99.22% used; 225841435 free inodes.

server3 `/tmp`: 292685537280 available bytes; 83.67% used; 114210523 free inodes.

server3 `/var/tmp`: 292685537280 available bytes; 83.67% used; 114210523 free inodes.
| server4 | True | ['2', '3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105932525568 available bytes; 94.09% used; 114348278 free inodes.

server4 `/home`: 105932525568 available bytes; 94.09% used; 114348278 free inodes.

server4 `/data`: 289763246080 available bytes; 96.00% used; 225388464 free inodes.

server4 `/tmp`: 105932525568 available bytes; 94.09% used; 114348278 free inodes.

server4 `/var/tmp`: 105932525568 available bytes; 94.09% used; 114348278 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
