# V2R cluster inventory

2026-09-24T09:38:34.638097+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324452503552 available bytes; 81.90% used; 112489777 free inodes.

server1 `/home`: 324452503552 available bytes; 81.90% used; 112489777 free inodes.

server1 `/tmp`: 324452503552 available bytes; 81.90% used; 112489777 free inodes.

server1 `/var/tmp`: 324452503552 available bytes; 81.90% used; 112489777 free inodes.

server1 `/mnt/raid5`: 501822156800 available bytes; 97.70% used; 337712365 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57764429824 available bytes; 96.78% used; 110430798 free inodes.

server2 `/home`: 57764429824 available bytes; 96.78% used; 110430798 free inodes.

server2 `/tmp`: 57764429824 available bytes; 96.78% used; 110430798 free inodes.

server2 `/var/tmp`: 57764429824 available bytes; 96.78% used; 110430798 free inodes.

server2 `/mnt/raid5`: 514334502912 available bytes; 96.45% used; 445177276 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85430648832 available bytes; 95.23% used; 114174401 free inodes.

server3 `/home`: 85430648832 available bytes; 95.23% used; 114174401 free inodes.

server3 `/data`: 165736452096 available bytes; 97.71% used; 225820387 free inodes.

server3 `/tmp`: 85430648832 available bytes; 95.23% used; 114174401 free inodes.

server3 `/var/tmp`: 85430648832 available bytes; 95.23% used; 114174401 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105757331456 available bytes; 94.10% used; 114349038 free inodes.

server4 `/home`: 105757331456 available bytes; 94.10% used; 114349038 free inodes.

server4 `/data`: 154574512128 available bytes; 97.86% used; 225273230 free inodes.

server4 `/tmp`: 105757331456 available bytes; 94.10% used; 114349038 free inodes.

server4 `/var/tmp`: 105757331456 available bytes; 94.10% used; 114349038 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
