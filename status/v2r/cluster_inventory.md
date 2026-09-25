# V2R cluster inventory

2026-09-25T08:48:14.534160+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318839586816 available bytes; 82.21% used; 112480391 free inodes.

server1 `/home`: 318839586816 available bytes; 82.21% used; 112480391 free inodes.

server1 `/tmp`: 318839586816 available bytes; 82.21% used; 112480391 free inodes.

server1 `/var/tmp`: 318839586816 available bytes; 82.21% used; 112480391 free inodes.

server1 `/mnt/raid5`: 364204822528 available bytes; 98.33% used; 337557042 free inodes.
| server2 | True | ['5', '6'] | [] | reference_compatible=False |

server2 `/`: 22833291264 available bytes; 98.73% used; 110410488 free inodes.

server2 `/home`: 22833291264 available bytes; 98.73% used; 110410488 free inodes.

server2 `/tmp`: 22833291264 available bytes; 98.73% used; 110410488 free inodes.

server2 `/var/tmp`: 22833291264 available bytes; 98.73% used; 110410488 free inodes.

server2 `/mnt/raid5`: 332685979648 available bytes; 97.70% used; 445093639 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84435660800 available bytes; 95.29% used; 114156049 free inodes.

server3 `/home`: 84435660800 available bytes; 95.29% used; 114156049 free inodes.

server3 `/data`: 142381285376 available bytes; 98.03% used; 225811385 free inodes.

server3 `/tmp`: 84435660800 available bytes; 95.29% used; 114156049 free inodes.

server3 `/var/tmp`: 84435660800 available bytes; 95.29% used; 114156049 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105633456128 available bytes; 94.11% used; 114350293 free inodes.

server4 `/home`: 105633456128 available bytes; 94.11% used; 114350293 free inodes.

server4 `/data`: 245018083328 available bytes; 96.61% used; 225001632 free inodes.

server4 `/tmp`: 105633456128 available bytes; 94.11% used; 114350293 free inodes.

server4 `/var/tmp`: 105633456128 available bytes; 94.11% used; 114350293 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
