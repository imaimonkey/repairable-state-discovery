# V2R cluster inventory

2026-09-23T16:15:33.748158+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41411022848 available bytes; 97.69% used; 110435185 free inodes.

server2 `/home`: 41411022848 available bytes; 97.69% used; 110435185 free inodes.

server2 `/tmp`: 41411022848 available bytes; 97.69% used; 110435185 free inodes.

server2 `/var/tmp`: 41411022848 available bytes; 97.69% used; 110435185 free inodes.

server2 `/mnt/raid5`: 549243408384 available bytes; 96.20% used; 445218328 free inodes.
| server3 | True | ['0'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 317861429248 available bytes; 82.26% used; 114295950 free inodes.

server3 `/home`: 317861429248 available bytes; 82.26% used; 114295950 free inodes.

server3 `/data`: 119456690176 available bytes; 98.35% used; 225854369 free inodes.

server3 `/tmp`: 317861429248 available bytes; 82.26% used; 114295950 free inodes.

server3 `/var/tmp`: 317861429248 available bytes; 82.26% used; 114295950 free inodes.
| server4 | True | ['1', '2', '3', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111498883072 available bytes; 93.78% used; 114375796 free inodes.

server4 `/home`: 111498883072 available bytes; 93.78% used; 114375796 free inodes.

server4 `/data`: 37390516224 available bytes; 99.48% used; 225486539 free inodes.

server4 `/tmp`: 111498883072 available bytes; 93.78% used; 114375796 free inodes.

server4 `/var/tmp`: 111498883072 available bytes; 93.78% used; 114375796 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
