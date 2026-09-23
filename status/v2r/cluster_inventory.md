# V2R cluster inventory

2026-09-23T17:10:33.873108+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41389821952 available bytes; 97.69% used; 110435441 free inodes.

server2 `/home`: 41389821952 available bytes; 97.69% used; 110435441 free inodes.

server2 `/tmp`: 41389821952 available bytes; 97.69% used; 110435441 free inodes.

server2 `/var/tmp`: 41389821952 available bytes; 97.69% used; 110435441 free inodes.

server2 `/mnt/raid5`: 546885607424 available bytes; 96.22% used; 445216593 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 294125912064 available bytes; 83.59% used; 114264187 free inodes.

server3 `/home`: 294125912064 available bytes; 83.59% used; 114264187 free inodes.

server3 `/data`: 53114667008 available bytes; 99.27% used; 225852455 free inodes.

server3 `/tmp`: 294125912064 available bytes; 83.59% used; 114264187 free inodes.

server3 `/var/tmp`: 294125912064 available bytes; 83.59% used; 114264187 free inodes.
| server4 | True | ['1', '2', '3', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111489466368 available bytes; 93.78% used; 114375792 free inodes.

server4 `/home`: 111489466368 available bytes; 93.78% used; 114375792 free inodes.

server4 `/data`: 29775405056 available bytes; 99.59% used; 225477579 free inodes.

server4 `/tmp`: 111489466368 available bytes; 93.78% used; 114375792 free inodes.

server4 `/var/tmp`: 111489466368 available bytes; 93.78% used; 114375792 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
