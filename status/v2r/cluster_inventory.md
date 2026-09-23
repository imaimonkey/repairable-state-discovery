# V2R cluster inventory

2026-09-23T18:10:05.059923+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41359966208 available bytes; 97.69% used; 110435428 free inodes.

server2 `/home`: 41359966208 available bytes; 97.69% used; 110435428 free inodes.

server2 `/tmp`: 41359966208 available bytes; 97.69% used; 110435428 free inodes.

server2 `/var/tmp`: 41359966208 available bytes; 97.69% used; 110435428 free inodes.

server2 `/mnt/raid5`: 545725870080 available bytes; 96.23% used; 445214755 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 293639643136 available bytes; 83.61% used; 114237507 free inodes.

server3 `/home`: 293639643136 available bytes; 83.61% used; 114237507 free inodes.

server3 `/data`: 52884787200 available bytes; 99.27% used; 225847848 free inodes.

server3 `/tmp`: 293639643136 available bytes; 83.61% used; 114237507 free inodes.

server3 `/var/tmp`: 293639643136 available bytes; 83.61% used; 114237507 free inodes.
| server4 | True | ['0', '1', '2', '3', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111487209472 available bytes; 93.78% used; 114375772 free inodes.

server4 `/home`: 111487209472 available bytes; 93.78% used; 114375772 free inodes.

server4 `/data`: 2834432 available bytes; 100.00% used; 225457217 free inodes.

server4 `/tmp`: 111487209472 available bytes; 93.78% used; 114375772 free inodes.

server4 `/var/tmp`: 111487209472 available bytes; 93.78% used; 114375772 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
