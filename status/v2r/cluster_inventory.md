# V2R cluster inventory

2026-09-23T17:50:15.133028+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41372319744 available bytes; 97.69% used; 110435442 free inodes.

server2 `/home`: 41372319744 available bytes; 97.69% used; 110435442 free inodes.

server2 `/tmp`: 41372319744 available bytes; 97.69% used; 110435442 free inodes.

server2 `/var/tmp`: 41372319744 available bytes; 97.69% used; 110435442 free inodes.

server2 `/mnt/raid5`: 546325573632 available bytes; 96.23% used; 445215584 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 294330101760 available bytes; 83.58% used; 114272090 free inodes.

server3 `/home`: 294330101760 available bytes; 83.58% used; 114272090 free inodes.

server3 `/data`: 52998541312 available bytes; 99.27% used; 225851658 free inodes.

server3 `/tmp`: 294330101760 available bytes; 83.58% used; 114272090 free inodes.

server3 `/var/tmp`: 294330101760 available bytes; 83.58% used; 114272090 free inodes.
| server4 | True | ['1', '2', '3', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111488491520 available bytes; 93.78% used; 114375784 free inodes.

server4 `/home`: 111488491520 available bytes; 93.78% used; 114375784 free inodes.

server4 `/data`: 4368453632 available bytes; 99.94% used; 225468726 free inodes.

server4 `/tmp`: 111488491520 available bytes; 93.78% used; 114375784 free inodes.

server4 `/var/tmp`: 111488491520 available bytes; 93.78% used; 114375784 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
