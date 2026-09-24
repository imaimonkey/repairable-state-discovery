# V2R cluster inventory

2026-09-24T09:12:10.281600+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324471812096 available bytes; 81.90% used; 112490011 free inodes.

server1 `/home`: 324471812096 available bytes; 81.90% used; 112490011 free inodes.

server1 `/tmp`: 324471812096 available bytes; 81.90% used; 112490011 free inodes.

server1 `/var/tmp`: 324471812096 available bytes; 81.90% used; 112490011 free inodes.

server1 `/mnt/raid5`: 503272337408 available bytes; 97.69% used; 337715517 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57778835456 available bytes; 96.78% used; 110430935 free inodes.

server2 `/home`: 57778835456 available bytes; 96.78% used; 110430935 free inodes.

server2 `/tmp`: 57778835456 available bytes; 96.78% used; 110430935 free inodes.

server2 `/var/tmp`: 57778835456 available bytes; 96.78% used; 110430935 free inodes.

server2 `/mnt/raid5`: 515151876096 available bytes; 96.44% used; 445178115 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85478543360 available bytes; 95.23% used; 114174262 free inodes.

server3 `/home`: 85478543360 available bytes; 95.23% used; 114174262 free inodes.

server3 `/data`: 166971273216 available bytes; 97.69% used; 225821258 free inodes.

server3 `/tmp`: 85478543360 available bytes; 95.23% used; 114174262 free inodes.

server3 `/var/tmp`: 85478543360 available bytes; 95.23% used; 114174262 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105758547968 available bytes; 94.10% used; 114349062 free inodes.

server4 `/home`: 105758547968 available bytes; 94.10% used; 114349062 free inodes.

server4 `/data`: 302826586112 available bytes; 95.81% used; 225273341 free inodes.

server4 `/tmp`: 105758547968 available bytes; 94.10% used; 114349062 free inodes.

server4 `/var/tmp`: 105758547968 available bytes; 94.10% used; 114349062 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
