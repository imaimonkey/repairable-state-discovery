# V2R cluster inventory

2026-09-23T17:25:49.444599+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41383129088 available bytes; 97.69% used; 110435441 free inodes.

server2 `/home`: 41383129088 available bytes; 97.69% used; 110435441 free inodes.

server2 `/tmp`: 41383129088 available bytes; 97.69% used; 110435441 free inodes.

server2 `/var/tmp`: 41383129088 available bytes; 97.69% used; 110435441 free inodes.

server2 `/mnt/raid5`: 547051585536 available bytes; 96.22% used; 445216278 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 294377304064 available bytes; 83.57% used; 114273798 free inodes.

server3 `/home`: 294377304064 available bytes; 83.57% used; 114273798 free inodes.

server3 `/data`: 53090738176 available bytes; 99.27% used; 225852153 free inodes.

server3 `/tmp`: 294377304064 available bytes; 83.57% used; 114273798 free inodes.

server3 `/var/tmp`: 294377304064 available bytes; 83.57% used; 114273798 free inodes.
| server4 | True | ['1', '2', '3', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111488913408 available bytes; 93.78% used; 114375784 free inodes.

server4 `/home`: 111488913408 available bytes; 93.78% used; 114375784 free inodes.

server4 `/data`: 24779837440 available bytes; 99.66% used; 225469101 free inodes.

server4 `/tmp`: 111488913408 available bytes; 93.78% used; 114375784 free inodes.

server4 `/var/tmp`: 111488913408 available bytes; 93.78% used; 114375784 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
