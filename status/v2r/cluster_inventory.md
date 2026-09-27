# V2R cluster inventory

2026-09-27T00:09:19.832324+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315430838272 available bytes; 82.40% used; 112445708 free inodes.

server1 `/home`: 315430838272 available bytes; 82.40% used; 112445708 free inodes.

server1 `/tmp`: 315430838272 available bytes; 82.40% used; 112445708 free inodes.

server1 `/var/tmp`: 315430838272 available bytes; 82.40% used; 112445708 free inodes.

server1 `/mnt/raid5`: 637711192064 available bytes; 97.07% used; 337408128 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 17938128896 available bytes; 99.00% used; 110367426 free inodes.

server2 `/home`: 17938128896 available bytes; 99.00% used; 110367426 free inodes.

server2 `/tmp`: 17938128896 available bytes; 99.00% used; 110367426 free inodes.

server2 `/var/tmp`: 17938128896 available bytes; 99.00% used; 110367426 free inodes.

server2 `/mnt/raid5`: 593700458496 available bytes; 95.90% used; 444957897 free inodes.
| server3 | True | ['3'] | [] | reference_compatible=True |

server3 `/`: 79812378624 available bytes; 95.55% used; 114068840 free inodes.

server3 `/home`: 79812378624 available bytes; 95.55% used; 114068840 free inodes.

server3 `/data`: 1349113217024 available bytes; 81.35% used; 225825922 free inodes.

server3 `/tmp`: 79812378624 available bytes; 95.55% used; 114068840 free inodes.

server3 `/var/tmp`: 79812378624 available bytes; 95.55% used; 114068840 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105879912448 available bytes; 94.09% used; 114347853 free inodes.

server4 `/home`: 105879912448 available bytes; 94.09% used; 114347853 free inodes.

server4 `/data`: 409573609472 available bytes; 94.34% used; 224823741 free inodes.

server4 `/tmp`: 105879912448 available bytes; 94.09% used; 114347853 free inodes.

server4 `/var/tmp`: 105879912448 available bytes; 94.09% used; 114347853 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
