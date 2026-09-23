# V2R cluster inventory

2026-09-23T16:47:39.283409+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41400320000 available bytes; 97.69% used; 110435439 free inodes.

server2 `/home`: 41400320000 available bytes; 97.69% used; 110435439 free inodes.

server2 `/tmp`: 41400320000 available bytes; 97.69% used; 110435439 free inodes.

server2 `/var/tmp`: 41400320000 available bytes; 97.69% used; 110435439 free inodes.

server2 `/mnt/raid5`: 548307566592 available bytes; 96.21% used; 445217508 free inodes.
| server3 | True | ['0'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 299948040192 available bytes; 83.26% used; 114286383 free inodes.

server3 `/home`: 299948040192 available bytes; 83.26% used; 114286383 free inodes.

server3 `/data`: 95331033088 available bytes; 98.68% used; 225853351 free inodes.

server3 `/tmp`: 299948040192 available bytes; 83.26% used; 114286383 free inodes.

server3 `/var/tmp`: 299948040192 available bytes; 83.26% used; 114286383 free inodes.
| server4 | True | ['1', '2', '3', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111498272768 available bytes; 93.78% used; 114375793 free inodes.

server4 `/home`: 111498272768 available bytes; 93.78% used; 114375793 free inodes.

server4 `/data`: 35694624768 available bytes; 99.51% used; 225477944 free inodes.

server4 `/tmp`: 111498272768 available bytes; 93.78% used; 114375793 free inodes.

server4 `/var/tmp`: 111498272768 available bytes; 93.78% used; 114375793 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
