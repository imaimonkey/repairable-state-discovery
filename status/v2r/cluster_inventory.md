# V2R cluster inventory

2026-09-24T08:58:06.960922+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324378636288 available bytes; 81.90% used; 112490174 free inodes.

server1 `/home`: 324378636288 available bytes; 81.90% used; 112490174 free inodes.

server1 `/tmp`: 324378636288 available bytes; 81.90% used; 112490174 free inodes.

server1 `/var/tmp`: 324378636288 available bytes; 81.90% used; 112490174 free inodes.

server1 `/mnt/raid5`: 503756288000 available bytes; 97.69% used; 337717174 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57788903424 available bytes; 96.78% used; 110430921 free inodes.

server2 `/home`: 57788903424 available bytes; 96.78% used; 110430921 free inodes.

server2 `/tmp`: 57788903424 available bytes; 96.78% used; 110430921 free inodes.

server2 `/var/tmp`: 57788903424 available bytes; 96.78% used; 110430921 free inodes.

server2 `/mnt/raid5`: 513790717952 available bytes; 96.45% used; 445178650 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 85899268096 available bytes; 95.21% used; 114199585 free inodes.

server3 `/home`: 85899268096 available bytes; 95.21% used; 114199585 free inodes.

server3 `/data`: 167093358592 available bytes; 97.69% used; 225821925 free inodes.

server3 `/tmp`: 85899268096 available bytes; 95.21% used; 114199585 free inodes.

server3 `/var/tmp`: 85899268096 available bytes; 95.21% used; 114199585 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105759490048 available bytes; 94.10% used; 114349082 free inodes.

server4 `/home`: 105759490048 available bytes; 94.10% used; 114349082 free inodes.

server4 `/data`: 319658377216 available bytes; 95.58% used; 225273411 free inodes.

server4 `/tmp`: 105759490048 available bytes; 94.10% used; 114349082 free inodes.

server4 `/var/tmp`: 105759490048 available bytes; 94.10% used; 114349082 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
