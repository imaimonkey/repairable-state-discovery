# V2R cluster inventory

2026-09-24T09:09:03.602475+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324475629568 available bytes; 81.90% used; 112490063 free inodes.

server1 `/home`: 324475629568 available bytes; 81.90% used; 112490063 free inodes.

server1 `/tmp`: 324475629568 available bytes; 81.90% used; 112490063 free inodes.

server1 `/var/tmp`: 324475629568 available bytes; 81.90% used; 112490063 free inodes.

server1 `/mnt/raid5`: 503502118912 available bytes; 97.69% used; 337715887 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57786052608 available bytes; 96.78% used; 110430945 free inodes.

server2 `/home`: 57786052608 available bytes; 96.78% used; 110430945 free inodes.

server2 `/tmp`: 57786052608 available bytes; 96.78% used; 110430945 free inodes.

server2 `/var/tmp`: 57786052608 available bytes; 96.78% used; 110430945 free inodes.

server2 `/mnt/raid5`: 515250851840 available bytes; 96.44% used; 445178427 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85478780928 available bytes; 95.23% used; 114175352 free inodes.

server3 `/home`: 85478780928 available bytes; 95.23% used; 114175352 free inodes.

server3 `/data`: 167007649792 available bytes; 97.69% used; 225821678 free inodes.

server3 `/tmp`: 85478780928 available bytes; 95.23% used; 114175352 free inodes.

server3 `/var/tmp`: 85478780928 available bytes; 95.23% used; 114175352 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105758818304 available bytes; 94.10% used; 114349076 free inodes.

server4 `/home`: 105758818304 available bytes; 94.10% used; 114349076 free inodes.

server4 `/data`: 318900813824 available bytes; 95.59% used; 225273381 free inodes.

server4 `/tmp`: 105758818304 available bytes; 94.10% used; 114349076 free inodes.

server4 `/var/tmp`: 105758818304 available bytes; 94.10% used; 114349076 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
