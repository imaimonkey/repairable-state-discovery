# V2R cluster inventory

2026-09-25T09:58:40.088654+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318838087680 available bytes; 82.21% used; 112480393 free inodes.

server1 `/home`: 318838087680 available bytes; 82.21% used; 112480393 free inodes.

server1 `/tmp`: 318838087680 available bytes; 82.21% used; 112480393 free inodes.

server1 `/var/tmp`: 318838087680 available bytes; 82.21% used; 112480393 free inodes.

server1 `/mnt/raid5`: 364744400896 available bytes; 98.33% used; 337556999 free inodes.
| server2 | True | ['6'] | [] | reference_compatible=False |

server2 `/`: 22827630592 available bytes; 98.73% used; 110410484 free inodes.

server2 `/home`: 22827630592 available bytes; 98.73% used; 110410484 free inodes.

server2 `/tmp`: 22827630592 available bytes; 98.73% used; 110410484 free inodes.

server2 `/var/tmp`: 22827630592 available bytes; 98.73% used; 110410484 free inodes.

server2 `/mnt/raid5`: 317118681088 available bytes; 97.81% used; 445091633 free inodes.
| server3 | True | ['3'] | [] | reference_compatible=True |

server3 `/`: 84420493312 available bytes; 95.29% used; 114156053 free inodes.

server3 `/home`: 84420493312 available bytes; 95.29% used; 114156053 free inodes.

server3 `/data`: 142237331456 available bytes; 98.03% used; 225810155 free inodes.

server3 `/tmp`: 84420493312 available bytes; 95.29% used; 114156053 free inodes.

server3 `/var/tmp`: 84420493312 available bytes; 95.29% used; 114156053 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105614458880 available bytes; 94.11% used; 114350276 free inodes.

server4 `/home`: 105614458880 available bytes; 94.11% used; 114350276 free inodes.

server4 `/data`: 240022233088 available bytes; 96.68% used; 224991929 free inodes.

server4 `/tmp`: 105614458880 available bytes; 94.11% used; 114350276 free inodes.

server4 `/var/tmp`: 105614458880 available bytes; 94.11% used; 114350276 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
