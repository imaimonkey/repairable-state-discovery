# V2R cluster inventory

2026-09-24T08:51:53.043778+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324383072256 available bytes; 81.90% used; 112490245 free inodes.

server1 `/home`: 324383072256 available bytes; 81.90% used; 112490245 free inodes.

server1 `/tmp`: 324383072256 available bytes; 81.90% used; 112490245 free inodes.

server1 `/var/tmp`: 324383072256 available bytes; 81.90% used; 112490245 free inodes.

server1 `/mnt/raid5`: 504004435968 available bytes; 97.69% used; 337717928 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57796587520 available bytes; 96.78% used; 110430940 free inodes.

server2 `/home`: 57796587520 available bytes; 96.78% used; 110430940 free inodes.

server2 `/tmp`: 57796587520 available bytes; 96.78% used; 110430940 free inodes.

server2 `/var/tmp`: 57796587520 available bytes; 96.78% used; 110430940 free inodes.

server2 `/mnt/raid5`: 514950295552 available bytes; 96.44% used; 445178958 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 85900480512 available bytes; 95.21% used; 114199581 free inodes.

server3 `/home`: 85900480512 available bytes; 95.21% used; 114199581 free inodes.

server3 `/data`: 167134195712 available bytes; 97.69% used; 225822040 free inodes.

server3 `/tmp`: 85900480512 available bytes; 95.21% used; 114199581 free inodes.

server3 `/var/tmp`: 85900480512 available bytes; 95.21% used; 114199581 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105759666176 available bytes; 94.10% used; 114349084 free inodes.

server4 `/home`: 105759666176 available bytes; 94.10% used; 114349084 free inodes.

server4 `/data`: 319809257472 available bytes; 95.58% used; 225273501 free inodes.

server4 `/tmp`: 105759666176 available bytes; 94.10% used; 114349084 free inodes.

server4 `/var/tmp`: 105759666176 available bytes; 94.10% used; 114349084 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
