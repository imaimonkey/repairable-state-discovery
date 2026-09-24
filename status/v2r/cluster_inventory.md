# V2R cluster inventory

2026-09-24T08:42:34.201425+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324390936576 available bytes; 81.90% used; 112490342 free inodes.

server1 `/home`: 324390936576 available bytes; 81.90% used; 112490342 free inodes.

server1 `/tmp`: 324390936576 available bytes; 81.90% used; 112490342 free inodes.

server1 `/var/tmp`: 324390936576 available bytes; 81.90% used; 112490342 free inodes.

server1 `/mnt/raid5`: 505537941504 available bytes; 97.68% used; 337719110 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57797783552 available bytes; 96.78% used; 110430966 free inodes.

server2 `/home`: 57797783552 available bytes; 96.78% used; 110430966 free inodes.

server2 `/tmp`: 57797783552 available bytes; 96.78% used; 110430966 free inodes.

server2 `/var/tmp`: 57797783552 available bytes; 96.78% used; 110430966 free inodes.

server2 `/mnt/raid5`: 515758780416 available bytes; 96.44% used; 445178997 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 85899214848 available bytes; 95.21% used; 114200226 free inodes.

server3 `/home`: 85899214848 available bytes; 95.21% used; 114200226 free inodes.

server3 `/data`: 173651365888 available bytes; 97.60% used; 225822291 free inodes.

server3 `/tmp`: 85899214848 available bytes; 95.21% used; 114200226 free inodes.

server3 `/var/tmp`: 85899214848 available bytes; 95.21% used; 114200226 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105768673280 available bytes; 94.10% used; 114349103 free inodes.

server4 `/home`: 105768673280 available bytes; 94.10% used; 114349103 free inodes.

server4 `/data`: 255326011392 available bytes; 96.47% used; 225288312 free inodes.

server4 `/tmp`: 105768673280 available bytes; 94.10% used; 114349103 free inodes.

server4 `/var/tmp`: 105768673280 available bytes; 94.10% used; 114349103 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
