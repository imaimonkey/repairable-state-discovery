# V2R cluster inventory

2026-09-23T17:18:11.689574+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41384091648 available bytes; 97.69% used; 110435440 free inodes.

server2 `/home`: 41384091648 available bytes; 97.69% used; 110435440 free inodes.

server2 `/tmp`: 41384091648 available bytes; 97.69% used; 110435440 free inodes.

server2 `/var/tmp`: 41384091648 available bytes; 97.69% used; 110435440 free inodes.

server2 `/mnt/raid5`: 546659815424 available bytes; 96.22% used; 445216498 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 294399475712 available bytes; 83.57% used; 114275956 free inodes.

server3 `/home`: 294399475712 available bytes; 83.57% used; 114275956 free inodes.

server3 `/data`: 53101821952 available bytes; 99.27% used; 225852302 free inodes.

server3 `/tmp`: 294399475712 available bytes; 83.57% used; 114275956 free inodes.

server3 `/var/tmp`: 294399475712 available bytes; 83.57% used; 114275956 free inodes.
| server4 | True | ['1', '2', '3', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111489347584 available bytes; 93.78% used; 114375792 free inodes.

server4 `/home`: 111489347584 available bytes; 93.78% used; 114375792 free inodes.

server4 `/data`: 26777587712 available bytes; 99.63% used; 225469201 free inodes.

server4 `/tmp`: 111489347584 available bytes; 93.78% used; 114375792 free inodes.

server4 `/var/tmp`: 111489347584 available bytes; 93.78% used; 114375792 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
