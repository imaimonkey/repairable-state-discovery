# V2R cluster inventory

2026-09-25T07:44:26.747482+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318864121856 available bytes; 82.21% used; 112480366 free inodes.

server1 `/home`: 318864121856 available bytes; 82.21% used; 112480366 free inodes.

server1 `/tmp`: 318864121856 available bytes; 82.21% used; 112480366 free inodes.

server1 `/var/tmp`: 318864121856 available bytes; 82.21% used; 112480366 free inodes.

server1 `/mnt/raid5`: 399588061184 available bytes; 98.17% used; 337558262 free inodes.
| server2 | True | ['0'] | [] |

server2 `/`: 22851125248 available bytes; 98.73% used; 110410475 free inodes.

server2 `/home`: 22851125248 available bytes; 98.73% used; 110410475 free inodes.

server2 `/tmp`: 22851125248 available bytes; 98.73% used; 110410475 free inodes.

server2 `/var/tmp`: 22851125248 available bytes; 98.73% used; 110410475 free inodes.

server2 `/mnt/raid5`: 334689480704 available bytes; 97.69% used; 445095913 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84439879680 available bytes; 95.29% used; 114156049 free inodes.

server3 `/home`: 84439879680 available bytes; 95.29% used; 114156049 free inodes.

server3 `/data`: 142391398400 available bytes; 98.03% used; 225812474 free inodes.

server3 `/tmp`: 84439879680 available bytes; 95.29% used; 114156049 free inodes.

server3 `/var/tmp`: 84439879680 available bytes; 95.29% used; 114156049 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105637421056 available bytes; 94.11% used; 114350351 free inodes.

server4 `/home`: 105637421056 available bytes; 94.11% used; 114350351 free inodes.

server4 `/data`: 249057910784 available bytes; 96.56% used; 225012177 free inodes.

server4 `/tmp`: 105637421056 available bytes; 94.11% used; 114350351 free inodes.

server4 `/var/tmp`: 105637421056 available bytes; 94.11% used; 114350351 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
