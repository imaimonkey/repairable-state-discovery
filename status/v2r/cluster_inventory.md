# V2R cluster inventory

2026-09-23T18:28:24.209796+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41354670080 available bytes; 97.69% used; 110435428 free inodes.

server2 `/home`: 41354670080 available bytes; 97.69% used; 110435428 free inodes.

server2 `/tmp`: 41354670080 available bytes; 97.69% used; 110435428 free inodes.

server2 `/var/tmp`: 41354670080 available bytes; 97.69% used; 110435428 free inodes.

server2 `/mnt/raid5`: 544916357120 available bytes; 96.23% used; 445214122 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 294186557440 available bytes; 83.58% used; 114268546 free inodes.

server3 `/home`: 294186557440 available bytes; 83.58% used; 114268546 free inodes.

server3 `/data`: 52860715008 available bytes; 99.27% used; 225847517 free inodes.

server3 `/tmp`: 294186557440 available bytes; 83.58% used; 114268546 free inodes.

server3 `/var/tmp`: 294186557440 available bytes; 83.58% used; 114268546 free inodes.
| server4 | True | ['0', '1', '2', '3', '4', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111419142144 available bytes; 93.78% used; 114373057 free inodes.

server4 `/home`: 111419142144 available bytes; 93.78% used; 114373057 free inodes.

server4 `/data`: 29102080 available bytes; 100.00% used; 225458136 free inodes.

server4 `/tmp`: 111419142144 available bytes; 93.78% used; 114373057 free inodes.

server4 `/var/tmp`: 111419142144 available bytes; 93.78% used; 114373057 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
